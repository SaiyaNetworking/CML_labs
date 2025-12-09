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
[Routers_ospf_20251203_125657.txt](https://github.com/SaiyaNetworking/CML_labs/blob/main/pyscripts/ospf_automation/Routers_ospf_20251203_125657.txt)

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

# OSPF automation part 2 - multi-area deployments, area summary routes and DR/BDR setups

`ospf_deployment__multiarea_automation.py` is a two-part script using an enumerated index to deploy OSPF to five different routers via telnet with the configurations of:
* OSPF 1 areas 0, 10 and 20
* 10.0.0.0/24 - 10.0.4.0/24 network range
* Loopback interfaces advertised on 192.168.100.0/24 - 192.168.104.0/24
* Autocost reference bandwidth of 100gbps
* Passive interface on R1's g0/2 interface
* R1
    * Route summarization of 10.0.0.0/16 for area 0
    * Route summarization of 192.168.1.0/24 for area 20 (external networks)
    * Gateway of last resort advertised
    * Set up as an Area Border Router (ABR)
* R2
    * Backbone router (area 0)
    * Designated Router (DR)
* R3
    * Backbone router
    * Backup Designated Router (BDR) 
* R4
    * Route summarization of 10.0.4.0/24 for area 10
    * Route summarization of 10.0.0.0/16 for area 0
* R5
  * Router with networks of 10.0.0.0/16 and 192.168.100.0/24 advertised on area 10
* A second loop of the script to use the "clear ip ospf process" command to elect the proper DR/BDR configurations

`ospf_configpull_automation.py` can also be used with this script with a sample printed out here: [Routers_ospf_areas_20251208_172128.txt](https://github.com/SaiyaNetworking/CML_labs/blob/main/pyscripts/ospf_automation/Routers_ospf_areas_20251208_172128.txt)

Prerequisites will be same as for part one

Cisco Modeling Lab (CML) yaml files `OSPF_automation_multi-area_preconfig.yaml` and `OSPF_automation_multi-area_postconfig.yaml` will be uploaded as pre-configured automation 
and post-configured automation labs

This is the lab topology used for the scripts

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/ospf_areas_topology.png)


