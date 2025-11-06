# OSPF automation - Netmiko

This is a basic script to deploy OSPF to three different routers via telnet. The purpose to to see if the third network 10.0.2.0/24 can be advertised and dynamically discovered through automated means.
Cisco Modeling Lab (CML) yaml files `Dynamic_Network_automation_deployment_ospf_preconfig` and `Dynamic_Network_automation_deployment_ospf_postconfig` will be uploaded as pre-configured automation 
and post-configured automation labs

### `ospf_netmiko.py`
Prerequisites to run the main script if repurposed will be:

``````````
# OSPF automation
# Prerequisites:
    # Static routes configured so all routers can reach each other while leaving the third network unrouted (network 10.0.2.0/24 for our example)
    # Username, password and EXEC password are all enabled
    # Telnet on vty lines 0 4 are enabled
    # vty lines are configured to login local
    # transport input all (or telnet) is set on vty lines
    # change the host, username, password and secret key value pair to your own configurations
``````````
### `iprouting_netmiko.py`
This script is to pull the "show ip route ospf" information from R1 and save as text file `Router1_ospf.txt` to verify R1 has dynamically learned network 10.0.2.0/24 from OSPF


