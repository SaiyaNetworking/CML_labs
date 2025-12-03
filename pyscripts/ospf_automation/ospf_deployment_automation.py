# OSPF automation deployment script for single area (area 0)

# Prerequisites:
    # Static routes configured so all routers can reach each other
    # Username, password and EXEC password are all enabled
    # Telnet on vty lines 0 4 are enabled
    # vty lines are configured to login local
    # transport input all (or telnet) is set on vty lines


from netmiko import ConnectHandler

# Define routers and their interfaces separately
routers = [                                                                 # List defining each router's connection details and interfaces
    {
        "connection": {                                                     # R1
            "device_type": "cisco_ios_telnet",                                  # Telnet
            "host": "192.168.1.34",                                             # Connecting interface's IP
            "username": "cisco",                                                # vty username
            "password": "cisco",                                                # vty password
            "secret": "cisco",                                                  # EXEC password
        },
        "interfaces": ["GigabitEthernet0/0", "GigabitEthernet0/1", "GigabitEthernet0/2"],
    },
    {
        "connection": {                                                    # R2
            "device_type": "cisco_ios_telnet",
            "host": "10.0.0.2",
            "username": "cisco",
            "password": "cisco",
            "secret": "cisco",
        },
        "interfaces": ["GigabitEthernet0/0", "GigabitEthernet0/2"],
    },
    {
        "connection": {                                                    # R3
            "device_type": "cisco_ios_telnet",
            "host": "10.0.1.2",
            "username": "cisco",
            "password": "cisco",
            "secret": "cisco",
        },
        "interfaces": ["GigabitEthernet0/1", "GigabitEthernet0/3"],
    },
    {
        "connection": {                                                     # R4
            "device_type": "cisco_ios_telnet",
            "host": "10.0.2.1",
            "username": "cisco",
            "password": "cisco",
            "secret": "cisco",
        },
        "interfaces": ["GigabitEthernet0/2", "GigabitEthernet0/3", "GigabitEthernet0/4"],
    },
    {
        "connection": {                                                     # R5
            "device_type": "cisco_ios_telnet",
            "host": "10.0.4.2",
            "username": "cisco",
            "password": "cisco",
            "secret": "cisco",
        },
        "interfaces": ["GigabitEthernet0/4"],
    },
]




# Loop through routers with index to apply passive-interface, area summarization and default-information oringinate commands on R1
for idx, router in enumerate(routers):
    print(f"\nConnecting to {router['connection']['host']} via Telnet...")
    connection = ConnectHandler(**router["connection"])
    connection.enable()


    # Build OSPF commands to advertise 10.0.0.0/16 network, 192.168.0.0/32 loopback interfaces and change default reference bandwidth
    ospf_commands = [
        "router ospf 1",
        "auto-cost reference-bandwidth 100000",                 # Set reference bandwidth to 100 Gbps
        "network 10.0.0.0 0.0.255.255 area 0",                  # Advertise 10.0.0.0/16 network
        "network 192.168.0.0 0.0.0.255 area 0"                  # Advertise 192.168.0.0/32 loopback interfaces
    ]

    # If this is the first router in the list (R1), add the passive-interface and summarization for Gi0/2
    if idx == 0:                                                          # Change the index number to apply on a different router in the list if needed, from 0 to 4 for routers 1 to 5
        ospf_commands.append("router ospf 1")
        ospf_commands.append("passive-interface GigabitEthernet 0/2")     # Make interface GigabitEthernet0/2 passive
        ospf_commands.append("area 0 range 10.0.0.0 255.255.0.0")         # 10.0.0.0/21 route summarization. Comment to remove from script.
        ospf_commands.append("default-information originate")             # Enable default route advertisement in OSPF (static route 0.0.0.0 0.0.0.0 192.168.1.1 is already preconfigured on R1)


    # Apply OSPF hello and hold timers in the routers list
    for intf in router["interfaces"]:
        ospf_commands.append(f"interface {intf}")                     # cycle through interfaces list for each router in the router list
        ospf_commands.append("ip ospf hello-interval 30")             # hello-interval set to 30 seconds (bumped up from default of 10 seconds)
        ospf_commands.append("ip ospf dead-interval 120")             # dead-interval set to 120 seconds (default is 4 times the hello interval)

    # Push config
    print(f"Pushing OSPF config to {router['connection']['host']}...")
    output = connection.send_config_set(ospf_commands)
    print(output)

    # Save config
    save_output = connection.save_config()
    print(save_output)

    connection.disconnect()
    print(f"Completed configuration on {router['connection']['host']}")



# End OSPF deployment script













