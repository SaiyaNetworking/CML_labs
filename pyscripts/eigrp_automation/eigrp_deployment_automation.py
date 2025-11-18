# EIGRP automation
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

# Loop through routers with index to apply passive-interface on R1 only on Gi0/2
for idx, router in enumerate(routers):
    print(f"\nConnecting to {router['connection']['host']} via Telnet...")
    connection = ConnectHandler(**router["connection"])
    connection.enable()


    # Build EIGRP commands to advertise 10.0.0.0/16 network
    eigrp_commands = [
        "router eigrp 100",
        "network 10.0.0.0 0.0.255.255"
    ]

    # If this is the first router in the list (R1), add the passive-interface and summarization for Gi0/2
    if idx == 0:                                                                             # Change the index number to apply on a different router in the list if needed, from 0 to 4 for routers 1 to 5
        eigrp_commands.append("passive-interface GigabitEthernet0/2")
        eigrp_commands.append("interface GigabitEthernet0/2")
        eigrp_commands.append("ip summary-address eigrp 100 10.0.0.0 255.255.248.0")         # 10.0.0.0/21 route summarization. Comment to remove from script.


    # Apply EIGRP hello and hold timers in the routers list
    for intf in router["interfaces"]:
        eigrp_commands.append(f"interface {intf}")                     # cycle through interfaces list for each router in the router list
        eigrp_commands.append("ip hello-interval eigrp 100 30")        # hello-interval set to 30 seconds
        eigrp_commands.append("ip hold-time eigrp 100 90")             # hold-time set to 90 seconds

    # Push config
    print(f"Pushing EIGRP config to {router['connection']['host']}...")
    output = connection.send_config_set(eigrp_commands)
    print(output)

    # Save config
    save_output = connection.save_config()
    print(save_output)

    connection.disconnect()
    print(f"Completed configuration on {router['connection']['host']}")



# End