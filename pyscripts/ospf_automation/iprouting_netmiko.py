# simple script to connect to a network device and run a command using netmiko
# This script spefically connects to a Cisco IOSv router and retrieves the running configuration.


from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios_telnet",   # IOSv
    "host": "192.168.1.34",       # Replace with your router IP
    "username": "cisco",          # Your SSH username
    "password": "cisco",          # Your SSH password
    "secret": "cisco",            # Enable password (same as login if not set separately)
}

# Connect to the device
connection = ConnectHandler(**device)

# Enter enable mode
connection.enable()

# Pull running config
output = connection.send_command("show ip route ospf")     # String input is the exact command to run on IOS console
print(output)

# Save output to a file
with open("Router1_ospf.txt", "w") as file:
    file.write(output)



# Disconnect
connection.disconnect()

