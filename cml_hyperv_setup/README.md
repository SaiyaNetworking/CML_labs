# Hyper-V Cisco Modeling Labs (CML) with external access (Breakout)




Behold! An alternative to the VMware setup.


Why Hyper-V?
- You already have a native Windows Environment
- You cannot use a Linux Environment
- You don't want to learn Linux (I would not recommend this. You will need Linux eventually.)
- Relatively straightforward to set up

Why not Hyper-V?
- External connection setup is not documented *anywhere* that I have seen for Hyper-V
- This is the only exception I have found: https://learningnetwork.cisco.com/s/question/0D56e0000CTrEQOCQ3/cml-24-running-inside-windows-2022-hyperv
   * _I personally cannot get this to work. I end up soft-locking the controller and losing access to the virtual interface_
- Have an easier time with pyATS on non-Windows environments
- VMware and Hyper-V do not coexist well and there will be bugs
- Cisco officially supports CML on VMware. Hyper-V is unofficial and relies on community-orientated support
- You can easily set up external connections on VMware


So it should be reiterated that yes, you can run CML quite well on Hyper-V environments, but to have external access is extremely convoluted and requires the use of Cisco's Breakout Tool for CML.
In layman's terms, you're using your PC as a next-hop to a localhost interface through the CML Breakout tool.

### 1) INSTALLATION OF CML

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

### 3) BREAKOUT TOOL SETUP

This is a setup* of the breakout tool from Aaron Gould's YT channel: https://www.youtube.com/watch?v=pHb9sC-k5Ss

- _*Note: I personally had issues setting the tool up following Mr. Gould's YT guide. I was just spinning my wheels because there was no initial
  .yaml config file the program could initially draw from. Step 3 is an addition to Mr. Gould's video if anyone else is having the same issues._


First, we need to set up the breakout tool. From the Tools dropdown meny, select "Breakout Tool":

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic10_breakout.png)


From the new page opened up, go to the download page on the left column and download the "breakout-windows-amd64.exe" program. Place the program in your directory of choice 
(I placed mine in the main directory of my CML files):

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic11_breakout.png)

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic12_breakout.png)

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic13_breakout.png)


If you try running the .exe, nothing will happen except Windows complaining about the .exe. The program will need to run in a command prompt terminal with this command:
- breakout-windows-amd64 ui

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic14_breakout.png)


Uh-oh. Looking at the output underneath, we can see we have a problem at the end of the output. "No passwords are provided, either set it in the configuration 
file or provide it via an environment variable (BREAKOUT_PASSWORD)"

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic15_breakout.png)


So where's our configuration file? There is none so we have to make one. Run this command in the terminal:
- breakout-windows-amd64 config string

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic16_breakout.png)


Lets try running the "breakout-windows-amd64 ui" command again and see if we can get in:

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic17_breakout.png)


Nothing. How come? The new config.yaml only has the default configurations and require you to manually input your own credentials. Open the config.yaml file 
with your favorite text editor:

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic18_breakout.png)

Under these parameters you want to type in your credentials and type in a new parameter "password":
- **controller: https://** *your controller's dns name*
 **username:** *controller's login name*
- **password:** *profile's password*
    * *Note: YAML is space-sensitive. Have a space after the colon for your password*

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic19_breakout.png)

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic20_breakout.png)



Be sure to save. Run the .exe again in the terminal using the command "breakout-windows-amd64 ui" (make sure CML is running in the background):

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic21_breakout.png)


Success!!! The program is up and running. Access the webUI by entering "localhost:8080" into your weburl (note: Chrome might not allow you to connect, 
try a different browser. I'm currently using Edge.)

...Huh. We're in the webUI but we have this x509: certificate error. We can't get into our labs. Go over to the config menu and disable the "verify TLS certificate" 
option. Be sure to save. You can also configure your ports and addresses here as well.

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic22_breakout.png)

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic23_breakout.png)


Go back to the labs menu. If you don't see a lab, use the refresh button and then select your lab:

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic24_breakout.png)

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic25_breakout.png)


Right now, you can see your serial interfaces are down for the telnet access. Disable and reenable them from the webUI:

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic26_breakout.png)

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic27_breakout.png)

### 4) TELNET ACCESS

Open up another cmd terminal and telnet* into one of the router interfaces by the localhost port (iosv-0/1 for our example here) using the command:
- telnet localhost 9000
   * _Change the port number to what you want to telnet into_
   * Note: You might need to enable telnet on windows: https://www.laptopmag.com/how-to/enable-and-use-telnet-on-windows-11
   * 
  ![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic28_telnet.png)



And we're in! You can see how the normal Cisco IOS commands work.

![alt text](https://github.com/SaiyaNetworking/CML_labs/blob/main/cml_hyperv_setup/pics/cml_hyperv_pic29_telnet.png)



Arguably a little more convoluted than VMware, but if for whatever reaon you cannot use VMware, this is another alternative. This is also the only way 
I have been able to configure external connections to be able to interact with the devices outside of the simulated network on Hyper-V. Hopefully Cisco 
will officially support Hyper-V or someone will produce a guide on how to properly configure exit connection for Hyper-V.





