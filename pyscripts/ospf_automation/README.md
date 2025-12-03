# OSPF automation part 1 - Netmiko

`ospf_deployment_automation.py` is a basic script using an enumerated index to deploy OSPF to five different routers via telnet with the configurations of:
* OSPF 1 area 0
* 10.0.0.0/24 - 10.0.4.0/24 network range
* Passive interface on R1's g0/2 interface
* A route summarization of 10.0.0.0/21 on R1's g0/2 interface
* Hello-interval 30-second timers on the appropriate interfaces
* Dead-interval 120-second timers on the appropriate interfaces

`ospf_configpull_automation.py` is a script using a nested for loop to pull ospf info from all five routers and append them into a 
.txt file with the commands of:
* "show running-config | section ospf"
* "show ip ospf neighbor"
* "show ip ospf database"
* "show ip ospf topology-info"
* Output text file named `Routers_ospf_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt`

A sample text file has also been uploaded showing the output of the configuration pull: 
(placeholder)

### `ospf_deployment_automation.py` and `ospf_configpull_automation.py`
Prerequisites to run the scripts if repurposed will be:
``````````
# OSPF automation
# Prerequisites:
    # Static routes configured so all routers can reach each other
    # Username, password and EXEC password are all enabled
    # Telnet on vty lines 0 4 are enabled
    # vty lines are configured to login local
    # transport input all (or telnet) is set on vty lines
    # change default route next-hop on R1 if needed
``````````
Cisco Modeling Lab (CML) yaml files `ospf_automation_preconfig.yaml` and `ospf_automation_postconfig.yaml` will be uploaded as pre-configured automation 
and post-configured automation labs

This is the lab topology used for the scripts

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/pyscripts/eigrp_automation/eigrp_topology.png)


## Part 2 will include multi-area deployments, area summary routes and DR/BDR setups
