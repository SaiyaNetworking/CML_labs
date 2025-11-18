# EIGRP automation - Netmiko

`eigrp_deployment_automation.py` is a basic script using an enumerated index to deploy EIGRP to five different routers via telnet with the configurations of:
* EIGRP Autonomous System 100
* 10.0.0.0/24 - 10.0.4.0/24 network range
* Passive interface on R1's g0/2 interface
* A route summarization of 10.0.0.0/21 on R1's g0/2 interface
* Hello-interval 30-second timers on the appropriate interfaces
* Hold-time 90-second timers on the appropriate interfaces

`eigrp_configpull_automation.py` is a script using a nested for loop to pull eigrp info from all five routers and append them into a 
.txt file with the commands of:
* "show running-config | section eigrp"
* "show ip eigrp neighbors"
* "show ip eigrp topology"
* "show ip eigrp topology all-links"
* Output text file named `Routers_eigrp_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt`

A sample text file has also been uploaded showing the output of the configuration pull: [Routers_eigrp_20251118_131418.txt](https://github.com/SaiyaNetworking/CML_labs/blob/main/pyscripts/eigrp_automation/Routers_eigrp_20251118_131418.txt)

### `eigrp_deployment_automation.py` and `eigrp_configpull_automation.py`
Prerequisites to run the scripts if repurposed will be:
``````````
# EIGRP automation
# Prerequisites:
    # Static routes configured so all routers can reach each other
    # Username, password and EXEC password are all enabled
    # Telnet on vty lines 0 4 are enabled
    # vty lines are configured to login local
    # transport input all (or telnet) is set on vty lines
``````````


Cisco Modeling Lab (CML) yaml files `EIGRP_automation_preconfig.yaml` and `EIGRP_automation_postconfig.yaml` will be uploaded as pre-configured automation 
and post-configured automation labs

This is the lab topology used for the scripts

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/pyscripts/eigrp_automation/eigrp_topology.png)
