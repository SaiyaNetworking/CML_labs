# OSPF automation deployment script for multi-area (areas 0 10 20)

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


    # Placeholder list to insert OSPF configuration commands in the idx loop
    ospf_commands = [
        "router ospf 1",
        "auto-cost reference-bandwidth 100000",                 # Set reference bandwidth to 100 Gbps
    ]

    # If this is the first router in the list (R1), add the passive-interface and summarization for Gi0/2
    # We will use this format to append to the ospf_commands list for the other routers as needed
    if idx == 0:                                                            # Change the index number to apply on a different router in the list if needed, from 0 to 4 for routers 1 to 5
        ospf_commands.append("router ospf 1")
        ospf_commands.append("passive-interface GigabitEthernet 0/2")       # Make interface GigabitEthernet0/2 passive
        ospf_commands.append("network 10.0.0.0 0.0.255.255 area 0")         # 10.0.0.0/16 in area 0
        ospf_commands.append("network 192.168.1.0 0.0.0.255 area 20")       # 192.168.1.0/24 in area 20
        ospf_commands.append("network 192.168.100.0 0.0.0.255 area 0")      # 192.168.100.0/32 loopbacks in area 0
        ospf_commands.append("default-information originate")               # Enable default route advertisement in OSPF (static route 0.0.0.0 0.0.0.0 192.168.1.1 is already preconfigured on R1)
        ospf_commands.append("area 20 range 192.168.1.0 255.255.255.0")     # Summarize area 20          
        ospf_commands.append("area 0 range 10.0.0.0 255.255.0.0")           # Summarize area 0

# R2
    if idx == 1:                                                            
        ospf_commands.append("router ospf 1")
        ospf_commands.append("network 10.0.0.0 0.0.255.255 area 0")
        ospf_commands.append("network 192.168.100.0 0.0.0.255 area 0")
        ospf_commands.append("int range g0/0,g0/2")                         # Interface range we want for Designated Router (DR)         
        ospf_commands.append("ip ospf priority 255")                        # 255 is highest priority to become DR

# R3
    if idx == 2:                                                            
        ospf_commands.append("router ospf 1")
        ospf_commands.append("network 10.0.0.0 0.0.255.255 area 0")
        ospf_commands.append("network 192.168.100.0 0.0.0.255 area 0")
        ospf_commands.append("int range g0/0,g0/3")                         # Interface range we want for Backup Designated Router (BDR)         
        ospf_commands.append("ip ospf priority 254")                        # 254 is highest priority to become BDR

# R4
    if idx == 3:                                                            
        ospf_commands.append("router ospf 1")
        ospf_commands.append("network 10.0.0.0 0.0.255.255 area 0")         
        ospf_commands.append("network 192.168.100.0 0.0.0.255 area 0")      
        ospf_commands.append("network 192.168.100.0 0.0.0.255 area 0")
        ospf_commands.append("network 10.0.4.0 0.0.255.255 area 10")
        ospf_commands.append("area 0 range 10.0.0.0 255.255.0.0")            
        ospf_commands.append("area 10 range 10.0.4.0 255.255.255.0")

# R5
    if idx == 4:                                                            
        ospf_commands.append("router ospf 1")
        ospf_commands.append("network 10.0.0.0 0.0.255.255 area 10")         
        ospf_commands.append("network 192.168.100.0 0.0.0.255 area 10") 
           

    # Push config
    print(f"Pushing OSPF config to {router['connection']['host']}...")
    output = connection.send_config_set(ospf_commands)
    print(output)

    # Save config
    save_output = connection.save_config()
    print(save_output)

    connection.disconnect()
    print(f"Completed configuration on {router['connection']['host']}")

# Reconnect to each router to clear OSPF process for DR/BDR election
for router in routers:
    print(f"\nReconnecting to {router['connection']['host']} to clear OSPF process...")
    connection = ConnectHandler(**router["connection"])
    connection.enable()

    clear_output = connection.send_command("clear ip ospf process", expect_string=r"[confirm]")
    clear_output += connection.send_command("\n")  # confirm
    print(clear_output)

    connection.disconnect()
    print(f"OSPF process cleared on {router['connection']['host']}")




# End OSPF deployment script













