# OSPF config pull
# Prerequisites:
    # Static routes configured so all routers can reach each other
    # Username, password and EXEC password are all enabled
    # Telnet on vty lines 0 4 are enabled
    # vty lines are configured to login local
    # transport input all (or telnet) is set on vty lines
    # This script piggybacks off of the ospf_deployment_automation.py script to pull OSPF data. Runs independently.


#------------------------------------------
# Import tools. Netmiko for network connectivity, datetime for the .txt file timestamp.
from netmiko import ConnectHandler
from datetime import datetime


#------------------------------------------
# List for routers. Change the values in the keys for your personal labs.
routers = [
    {
        "name": "R1",                               # Router name
        "connection": {                             # Connection object list
            "device_type": "cisco_ios_telnet",      # IOS image using telnet connection
            "host": "192.168.1.34",                 # interface IP you want to telnet to
            "username": "cisco",                    # username
            "password": "cisco",                    # password
            "secret": "cisco",                      # EXEC password
        },
    },
    {
        "name": "R2",
        "connection": {
            "device_type": "cisco_ios_telnet",
            "host": "10.0.0.2",
            "username": "cisco",
            "password": "cisco",
            "secret": "cisco",
        },
    },
    {
        "name": "R3",
        "connection": {
            "device_type": "cisco_ios_telnet",
            "host": "10.0.1.2",
            "username": "cisco",
            "password": "cisco",
            "secret": "cisco",
        },
    },
    {
        "name": "R4",
        "connection": {
            "device_type": "cisco_ios_telnet",
            "host": "10.0.2.1",
            "username": "cisco",
            "password": "cisco",
            "secret": "cisco",
        },
    },
    {
        "name": "R5",
        "connection": {
            "device_type": "cisco_ios_telnet",
            "host": "10.0.4.2",
            "username": "cisco",
            "password": "cisco",
            "secret": "cisco",
        },
    },
]

#------------------------------------------------
# Array to hold all of the commands we want to run
commands = [                                                                    # Variable to hold the commands we want to run
    "show running-config | section ospf",
    "show ip ospf neighbor",
    "show ip ospf database",
    "show ip ospf topology-info",
]

#------------------------------------------------
# Create a print variable with a timestamp
outfile = f"Routers_ospf_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"        # Variable to print out the text file with a timestamp




#-------------------------------------------------
# This is a nested for loop to reiterate through all of our commands for each router

for r in routers:
    host = r["connection"]["host"]                                                                  # Stores key:value pairs into the host variable
    name = r.get("name", host)                                                                      # Pull the name key:value pair from the routers list. if not, then uses the host variable as a name.
    try:
        print(f"Connecting to {name} ({host})...")                                                  # Print out in the terminal to show something is happening....
        conn = ConnectHandler(**r["connection"])                                                    # Opens a session to the device in the routers list
        conn.enable()                                                                               # Runs the "enable" command on the IOS device to get in EXEC mode

        results = []                                                                                # Initializes an empty list to collect the output text.
        results.append(f"=== {name} ({host}) - collected at {datetime.now().isoformat()} ===\n")    # Header in text file with the name, IP and time stamp

        for cmd in commands:                                                                        # Inner loop to go over the "show" commands in the commands array
            results.append(f"--- {cmd} ---\n")                                                      # Another header for the text file to separate show commands
            out = conn.send_command(cmd)                                                            # Captures the output
            results.append(out + "\n\n")                                                            # Appends the output plus an extra line for readibility

        conn.disconnect()                                                                           # Exit the device's session

        # Append to file
        with open(outfile, "a") as fh:
            fh.writelines(results)                                                                  # Writes out the collected info into a neat structure with line breaks

        print(f"Completed {name} ({host}) - results appended to {outfile}")                         # Prints in the terminal letting you know the data collection is complete

    except Exception as e:
        print(f"Error connecting to {name} ({host}): {e}")                                          # If a failure happens, the terminal will print out the connection fault and move to the next router





#end