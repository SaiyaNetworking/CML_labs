# Hyper-V Cisco Modeling Labs (CML) v2.9 with external access



Behold! An alternative to the VMware setup.


Why Hyper-V?
- You already have a native Windows Environment
- You cannot use a Linux Environment
- You don't want to learn Linux (I would not recommend this. You will need Linux.)
- Relatively straightforward to set up
- Windows Subsystem for Linux (WSL) interacts real well with CML
- Your entire Windows lab environment can be on one host device under Hyper-V

Why not Hyper-V?
- External connection setup is not documented *anywhere* that I have seen for Hyper-V...except here and one other place
- This is the only exception I have found: https://learningnetwork.cisco.com/s/question/0D56e0000CTrEQOCQ3/cml-24-running-inside-windows-2022-hyperv
- Have an easier time with pyATS on non-Windows environments
- VMware and Hyper-V do not coexist well and there will be bugs
- Cisco officially supports CML on VMware. Hyper-V is unofficial and relies on community-orientated support

As far as I'm aware, I'm only one of the few people to set up a functional CML environment using Microsoft's Hyper-V environment. Though to save time on redundancy,
the installations of CML and WSL will be reference outside of github

---

## Table of Contents

1) INSTALLATION OF CML
2) LICENSE ACTIVATION
3) CHANGE WINDOWS NETWORK SETTINGS
4) INSTALLATION OF WSL
5) PYATS and GENIE INSTALLATION
6) GENIE and YAML
7) MISC RESOURCES

----

### 1) INSTALLATION OF CML

_Note: use an ethernet connection to reliably receive DHCP requests through the spoofed MAC addresses option from Hyper-V's VM. Unless your wireless network setup can support full-bridge MAC spoofing,
 your external DHCP server will not be able to lease out DHCP requests from CML!_

First, installation of CML to Hyper-V. We will reference this website which has an in-depth installation guide: 
- https://www.networkacademy.io/ccna/network-fundamentals/cml-on-hyperv
- Archive of the site: https://web.archive.org/web/20251024184003/https://www.networkacademy.io/ccna/network-fundamentals/cml-on-hyperv

### 2) LICENSE ACTIVATION (skip if using free license)

Follow through the entire walkthrough until you can log into the webUI itself. If you're using a personal or personal+ license, just replace the free .iso's with your supplemented ones. 
You will need to enable the license through the webUI of CML:
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic1_license.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic2_license.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic3_license.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic4_license.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic5_license.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic6_license.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic7_license.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic8_license.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic9_license.png)

### 3) CHANGE WINDOWS NETWORK SETTINGS

_Note: After this step is complete you will have full functionality of CML through Hyper-V. Steps 4 and onward are for setting up a dev environment for automation purposes._

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic30_networksettings.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic31_networksettings.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic32_networksettings.png)


### 4) INSTALLATION OF WSL

We will use Microsoft themselves as our reference guide for WSL: https://windowsforum.com/threads/install-and-use-windows-subsystem-for-linux-wsl-for-dev-workflows.383254/

### 5) PYATS and GENIE INSTALLATION

Mr Richard Kileen wrote an excellent blog series about his setup for pyats which was the framework that I used: https://richardkilleen.co.uk/blog/category/cisco-pyats/

Specifically for this section, I want to add an extra repository to manage python versions without having to break global configurations within WSL. You will also need a code editor (I will use VSCode for our example).
This is also not a fully comprehensive guide but rather a straightforward installation method. If issues crop up, I would recommend review Richar Killeen's blog for the sake of brevity.

After setting up your WSL environment, open up WSL using the "WSL ~" command in your startup bar (We use WSL ~ to open to the user directory of WSL instead of the SYSTEM32 directory of windows)

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic33_pyats.png)

Type "pwd" (print working directory) to verify you're in your WSL directory. It should be /home/[username]

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic34_pyats.png)

Update and upgrade if you need to.

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic35_pyats.png)

After any updates, what will follow is a series of commands to:
1. Add the deadsnakes repository to allow older versions of python to be installed in virtual environments (venvs)
2. Install python versions 3.7-3.10 in a venv (we will use 3.10 for our example)
3. Create and setup a venv
4. Install the pyats and genie framework
5. Run some test scripts to verify functionality

Commands will be inlined for ease of input (change variables if needed)

`sudo add-apt-repository ppa:deadsnakes/ppa`

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic36_pyats.png)

`sudo apt install python3.10 python3.10-dev python3.10-venv -y`

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic37_pyats.png)

`python3.10 -m venv pyatsnew`

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic38_pyats.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic39_pyats.png)

`source pyatsnew/bin/activate`

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic40_pyats.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic41_pyats.png)

`python3 --version`

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic42_pyats.png)

`pip install pyats"[full]"`

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic43_pyats.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic44_pyats.png)




Open your code editor (I'll be using VSCode) _(note: be sure to have any extensions installed like Python3 if you're using VSCode. Code snippets will also be available at
Richard Killeen's blog post: https://richardkilleen.co.uk/blog/cisco-pyats/complete-guide-to-installing-pyats/)_

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic45_pyats.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic46_pyats.png)

Here's a code snippet for the dependecies

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic47_pyats.png)

This is the vibe-coded installation-test script. I don't know why it works but it does:

``````````````````````````````````
# AI-updated to run the pyats 25.9 version. Thanks Copilot.

# installation_test.py
from pyats.topology import loader
from pyats import aetest
import logging

# Set up logging so we can see what's happening
logging.basicConfig(level=logging.INFO)

class InstallationTest(aetest.Testcase):
    
    @aetest.test
    def test_imports(self):
        """Test that we can import the main pyATS modules"""
        try:
            from pyats import aetest
            from pyats.topology import loader
            from genie.conf import Genie
            self.passed("All imports successful")
        except ImportError as e:
            self.failed(f"Import failed: {e}")
    
    @aetest.test
    def test_genie_parsers(self):
        """Test that Genie parsers are available"""
        try:
            # Import basic parser module to verify installation
            import genie.libs.parser
            
            # Try to access the parser package
            if hasattr(genie.libs, 'parser'):
                self.passed("Genie parsers package is available")
            else:
                self.failed("Genie parsers package not found")
        except ImportError as e:
            self.failed(f"Error accessing parsers: {e}")

if __name__ == '__main__':
    aetest.main()

`````````````````````````````````````````````````````
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic48_pyats.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic49_pyats.png)


### 6) GENIE and YAML

Great news! You set up your dev environment (always an ardous task) and your dependancies are working. Before we move any further, you should set up a simple lab on CML and verify you can 
ping your router. Your router will also need:
1) A reachable interface (use the IP address)
2) A hostname
3) A local account
4) Password enabled for user EXEC mode
5) Your vty lines accessible from ssh or telnet (we will use login local)

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic50_genie.png)

After verifying you can telnet/ssh (we will use telnet for our example) into your device, lets set up a testbed file using Genie's interactive framework in the WSL terminal.

`genie create testbed interactive --output testbed1.yaml`

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic51_genie.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic52_genie.png)

Perfect, Genie created our yaml testbed file. Lets open it up and see what was configured:

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic53_genie.png)

Excellent, a .yaml file with proper syntax has been created. If anything needs to be changed, you can edit this testbed file for IP changes, user accounts, 
or even add more info for larger scripts. Lets run a test script:

`genie parse all --testbed-file testbed1.yaml --output all`

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic54_genie.png)
![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic55_genie.png)


Here is our Genie parse output:

``````````````````````````````````````````

2025-10-28 16:09:27,212: %UNICON-INFO: +++ R1 logfile all/connection_R1.txt +++

2025-10-28 16:09:27,213: %UNICON-INFO: +++ Unicon plugin generic (unicon.plugins.generic) +++
Trying 192.168.1.206...


2025-10-28 16:09:27,243: %UNICON-INFO: +++ connection to spawn: telnet 192.168.1.206, id: 130772379710368 +++

2025-10-28 16:09:27,243: %UNICON-INFO: connection to R1
Connected to 192.168.1.206.
Escape character is '^]'.

**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************

User Access Verification

Username: cisco
Password: 
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************
R1>

2025-10-28 16:09:28,314: %UNICON-INFO: Storing credentials from default as current_credentials

2025-10-28 16:09:28,315: %UNICON-INFO: +++ initializing handle +++
enable
Password: 
R1#

2025-10-28 16:09:28,458: %UNICON-INFO: +++ R1 with via 'cli': executing command 'term length 0' +++
term length 0
R1#

2025-10-28 16:09:28,674: %UNICON-INFO: +++ R1 with via 'cli': executing command 'term width 0' +++
term width 0
R1#

2025-10-28 16:09:28,888: %UNICON-INFO: +++ R1 with via 'cli': executing command 'show version' +++
show version
Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.9(3)M10, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Thu 01-Aug-24 12:32 by mcpre


ROM: Bootstrap program is IOSv

R1 uptime is 5 hours, 29 minutes
System returned to ROM by reload
System image file is "flash0:/vios-adventerprisek9-m"
Last reload reason: Unknown reason



This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco IOSv (revision 1.0) with  with 460013K/62464K bytes of memory.
Processor board ID 9QUMBLI4FMFOM6BEKV02L
4 Gigabit Ethernet interfaces
DRAM configuration is 72 bits wide with parity disabled.
256K bytes of non-volatile configuration memory.
2097152K bytes of ATA System CompactFlash 0 (Read/Write)
0K bytes of ATA CompactFlash 1 (Read/Write)
11264K bytes of ATA CompactFlash 2 (Read/Write)
0K bytes of ATA CompactFlash 3 (Read/Write)



Configuration register is 0x0

R1#

2025-10-28 16:14:40,832: %UNICON-INFO: +++ R1 logfile all/connection_R1.txt +++

2025-10-28 16:14:40,833: %UNICON-INFO: +++ Unicon plugin generic (unicon.plugins.generic) +++
Trying 192.168.1.206...


2025-10-28 16:14:40,852: %UNICON-INFO: +++ connection to spawn: telnet 192.168.1.206, id: 127690570773504 +++

2025-10-28 16:14:40,852: %UNICON-INFO: connection to R1
Connected to 192.168.1.206.
Escape character is '^]'.

**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************

User Access Verification

Username: cisco
Password: 
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************
R1>

2025-10-28 16:14:41,924: %UNICON-INFO: Storing credentials from default as current_credentials

2025-10-28 16:14:41,926: %UNICON-INFO: +++ initializing handle +++
enable
Password: 
R1#

2025-10-28 16:14:42,073: %UNICON-INFO: +++ R1 with via 'cli': executing command 'term length 0' +++
term length 0
R1#

2025-10-28 16:14:42,288: %UNICON-INFO: +++ R1 with via 'cli': executing command 'term width 0' +++
term width 0
R1#

2025-10-28 16:14:42,501: %UNICON-INFO: +++ R1 with via 'cli': executing command 'show version' +++
show version
Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.9(3)M10, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Thu 01-Aug-24 12:32 by mcpre


ROM: Bootstrap program is IOSv

R1 uptime is 5 hours, 34 minutes
System returned to ROM by reload
System image file is "flash0:/vios-adventerprisek9-m"
Last reload reason: Unknown reason



This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco IOSv (revision 1.0) with  with 460013K/62464K bytes of memory.
Processor board ID 9QUMBLI4FMFOM6BEKV02L
4 Gigabit Ethernet interfaces
DRAM configuration is 72 bits wide with parity disabled.
256K bytes of non-volatile configuration memory.
2097152K bytes of ATA System CompactFlash 0 (Read/Write)
0K bytes of ATA CompactFlash 1 (Read/Write)
11264K bytes of ATA CompactFlash 2 (Read/Write)
0K bytes of ATA CompactFlash 3 (Read/Write)



Configuration register is 0x0

R1#
`````````````````````````````````````````````````````

And there you have it! You set up a complete homelab environment with devops capabilities on a Windows Host machine. May this guide help you with your networking career.



### 7) MISC RESOURCES

These are just miscellaneous resources that can be referenced:

Cisco Modeling Labs https://www.cisco.com/site/us/en/learn/training-certifications/training/modeling-labs/index.html \
Cisco Learning Network https://learningnetwork.cisco.com/s/  \
CML installation guide https://www.networkacademy.io/ccna/network-fundamentals/cml-on-hyperv \
Archive of CML installation guide https://web.archive.org/web/20251024184003/https://www.networkacademy.io/ccna/network-fundamentals/cml-on-hyperv  \
Microsoft site of WSL installation guide https://windowsforum.com/threads/install-and-use-windows-subsystem-for-linux-wsl-for-dev-workflows.383254/ \
Richard Killeen's blog for pyats and python scripts: https://richardkilleen.co.uk/blog/category/cisco-pyats/ \
Richard Killeen's pyats installation guide: https://richardkilleen.co.uk/blog/cisco-pyats/complete-guide-to-installing-pyats/ \
Cisco pyATS whitepapers: https://developer.cisco.com/docs/pyats/api/ \
Cisco Genie whitepapers: https://developer.cisco.com/docs/genie-docs/ \
Cisco DevNet sandbox: https://developer.cisco.com/sandbox.html?ReturnUrl=https://devnetsandbox.cisco.com \







