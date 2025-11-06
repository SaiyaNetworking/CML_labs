# OSPF automation
# Prerequisites:
    # Static routes configured so all routers can reach each other while leaving the third network unrouted (network 10.0.2.0/24 for our example)
    # Username, password and EXEC password are all enabled
    # Telnet on vty lines 0 4 are enabled
    # vty lines are configured to login local
    # transport input all (or telnet) is set on vty lines


from netmiko import ConnectHandler

# Define routers and their interfaces separately
routers = [                                                                 # List defining each router's connection details and interfaces
    {
        "connection": {
            "device_type": "cisco_ios_telnet",                              # Telnet
            "host": "192.168.1.34",                                         # Connecting interface's IP
            "username": "cisco",                                            # vty username
            "password": "cisco",                                            # vty password
            "secret": "cisco",                                              # EXEC password
        },
        "interfaces": ["GigabitEthernet0/0", "GigabitEthernet0/1"],         # Interfaces to apply OSPF on
    },
    {
        "connection": {
            "device_type": "cisco_ios_telnet",
            "host": "10.0.0.2",
            "username": "cisco",
            "password": "cisco",
            "secret": "cisco",
        },
        "interfaces": ["GigabitEthernet0/0", "GigabitEthernet0/1"],
    },
    {
        "connection": {
            "device_type": "cisco_ios_telnet",
            "host": "10.0.1.2",
            "username": "cisco",
            "password": "cisco",
            "secret": "cisco",
        },
        "interfaces": ["GigabitEthernet0/0", "GigabitEthernet0/1"],
    }
]

# Loop through routers
for router in routers:
    print(f"\nConnecting to {router['connection']['host']} via Telnet...")
    connection = ConnectHandler(**router["connection"])
    connection.enable()

    # Build OSPF commands to advertise 10.0.0.0/16 network
    ospf_commands = [
        "router ospf 1",
        "network 10.0.0.0 0.0.255.255 area 0"
    ]

    # Apply OSPF to interfaces in the routers list
    for intf in router["interfaces"]:
        ospf_commands.append(f"interface {intf}")
        ospf_commands.append("ip ospf 1 area 0")

    # Push config
    print(f"Pushing OSPF config to {router['connection']['host']}...")
    output = connection.send_config_set(ospf_commands)
    print(output)

    # Save config
    save_output = connection.save_config()
    print(save_output)

    connection.disconnect()
    print(f"Completed configuration on {router['connection']['host']}")
