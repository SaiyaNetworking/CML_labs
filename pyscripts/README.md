# Simplified Python Network Automation - Netmiko

### SCOPE - PURPOSE OF THESE SCRIPTS
The purpose of these scripts are to introduce a framework for very simplistic, straightforward network configurations and automation for beginners using the Netmiko library. 
The showcased script in this tutorial will serve as a proof-of-concept for both the ability to request and pull data from a remote (Cisco) device.

### BACKGROUND - WHAT HAS WORKED BEST?
Some of the biggest issues that I have observed when it came to setting up automation deployments were:
  1. It's assumed you have a previous background in programming
  2. If not assumed, then it's the standard tutorial of:
     1. Skipping over how to set up your dev environment (or at least a very anemic overview) 
     2. Going over an extreme, tedious minutiae of starting concepts
     3. Immediately rushing into advanced concepts
  3. Long hours troubleshooting dependency issues just to get started

A network engineer is more interested in seeing how automated tasks can be leveraged for efficiency, not on how Larry's Audi can fit into the millionth 
list you've written from that same tutorial everyone recommends or spending hours debugging broken dependencies. There is also the fact that not every 
company might have the resources or means of having dedidated DevOps and CI/CD pipelines to assist the network engineer. These are some of the setups 
I've tried and what I ultimately found to be the most simplistic and robust:

  * __pyATS and Genie,__ a python framework designed by Cisco for Cisco. I personally have ran into multiple dependency issues, outdated instructions, unsupported 
  version issues, and general incompatibility issues with Genie framework itself. The dev environment is also an unwelcome experience to set up and in my opinion, not worth the frustration 
  and the worry that a single update will break absolutely everything. Undoubtedly pyATS Genie is a good framework because Cisco is the global trendsetter, but I 
  believe the difficulty in setting up a dev environent will frustrate your average beginner.

  * __Ansible__ has been the most robust with less overhead than Genie, but also requires a yaml testbed setup (Ansible calls these playbooks). You will need to know both yaml and python syntax.

  * __NAPALM__ as far as I'm aware doesn't have native IOS support but does have the ability to provide multi-vendor support with its abstracted API on top of other API's. Due to this niche,
  NAPALM will be outside of the scope of our objective (this doesn't invalidate NAPALM as a good freamework, though.)

  * __Netmiko__ has been the most straightforward and simplistic library I've worked with. Everything just works. Perfect for someone starting out in automation tasks.

### PREREQUISITES - WHAT YOU NEED TO START

In order to start using Netmiko for network automation, we want to verify the prerequisites needed for our dev environment:
  * Linux environment (Windows Subsystem for Linux works well and will be used in this example)
  * python virtual environment (venv)
  * Preferred IDE (VSCode will be used)
  * Devices to communicate with via ssh (We will use CML here)

## TUTORIAL

### PYTHON VENV SETUP

Start off by setting up your virtual python environment:

`python3 -m venv netmiko_scripts`

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_netmiko_pic1_venv.png)

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_netmiko_pic2_venv.png)

`source netmiko_scripts/bin/activate`

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_netmiko_pic3_venv.png)

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_netmiko_pic4_venv.png)

`pip install netmiko`

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_netmiko_pic5_venv.png)

### SCRIPT

Start up your IDE

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_netmiko_pic6_script.png)

This specific python script (listed below the picture) is going to pull whatever text output your Cisco IOS device prints out. You yourself will need to:
  * input your own IP address that you're reaching out to
  * the username configured for your device
  * the password for your username
  * the password for the EXEC-login (the key value is secret for this script)
  * Change the name of the text output in line 26 if you want to.


![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_netmiko_pic7_script.png)


```````````````````````````````````````````````
# simple script to connect to a network device and run a command using netmiko
# This script spefically connects to a Cisco IOSv router and retrieves the running configuration.


from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",   # IOSv
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
output = connection.send_command("show running-config")     # String input is the exact command to run on IOS console
print(output)

# Save output to a file
with open("Router1_running_config.txt", "w") as file:
    file.write(output)



# Disconnect
connection.disconnect()
`````````````````````````````````````````````````

Run the python script and see the results:

`python runconf_netmiko.py`

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_netmiko_pic8_script.png)

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_netmiko_pic9_script.png)

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_netmiko_pic10_script.png)


Not even 20 minutes later and you already have a functional script that can pull information from a remote device! In my opinion, Netmiko sets the gold 
standard on how simple network automation should be
