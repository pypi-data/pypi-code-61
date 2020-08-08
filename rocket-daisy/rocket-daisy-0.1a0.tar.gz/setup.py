# +---------------------------------------------------------------------------+
#
#      Program:    setup.py
#
#      Purpose:    setup for remote open control key enabling technology (Rocket)
#
#      Target:     ARMV61A
#
#      Author:     Martin Shishkov
#
#      License:    GPL 3
# +---------------------------------------------------------------------------+

import atexit
import os
import sys
from setuptools import setup
from setuptools.command.install import install
import re
import shutil
import io

daisy = "daisy"

with io.open("README.md", "r") as fh:
    long_description = fh.read()

def logo():
    print()
    print("                                          ")
    print("######                                    ")
    print("#     #  ####   ####  #    # ###### ##### ")
    print("#     # #    # #    # #   #  #        #   ")
    print("######  #    # #      ####   #####    #   ")
    print("#   #   #    # #      #  #   #        #   ")
    print("#    #  #    # #    # #   #  #        #   ")
    print("#     #  ####   ####  #    # ######   #   ")
    print("                                          ")


class CustomInstall(install):
    def run(self):
        def _post_install():

            setupDir = os.getcwd()
            logo()
            get_hostapd()
            get_config_dnsmasq("dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h")
            os.system("systemctl stop dnsmasq")
            os.system("systemctl stop hostapd")
            configure_hostapd()
            make_reliable_init_hostapd(setupDir, "192.168.4.1")
            os.system("systemctl stop wpa_supplicant")
            os.system("systemctl disable wpa_supplicant")
            os.system("systemctl mask wpa_supplicant")
            install_daisy(setupDir)
            adjust_http_docroot(setupDir, "script.py")
                
            if (adjust_rocketlauncher(setupDir) == -1):
                adjust_http_docroot(setupDir, "maxmotion.py")
                get_maxmotion_lib(setupDir)
                print("Start the demo with:\n sudo daisy -d -c /etc/daisy/config")
            else:
                activate_COM()

        atexit.register(_post_install)
        install.run(self)


setup(name='rocket-daisy',
      version='0.1a0',
      description='Remote open control key enabling technology (Rocket)',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/gulliversoft/rocket',
      author='gulliversoft',
      author_email='fg7@gulliversoft.com',
      license='GPL3',
      packages=['rocket','rocketlauncher',"rocket.daisy",
      "rocket.daisy.utils",
      "rocket.daisy.clients",
      "rocket.daisy.protocols",
      "rocket.daisy.server",
      "rocket.daisy.decorators",
      "rocket.daisy.devices",
      "rocket.daisy.devices.digital",
      "rocket.daisy.devices.analog",
      "rocket.daisy.devices.sensor",
      "rocket.daisy.devices.shield"],
      zip_safe=False,
      classifiers=["Intended Audience :: Education",
               'Development Status :: 3 - Alpha',
               'Programming Language :: Python :: 3', 
               "Operating System :: POSIX :: Linux",
               'Topic :: Software Development',
               'Topic :: Home Automation',
               'Topic :: System :: Hardware'],
      cmdclass={'install': CustomInstall})
      #install_requires[''])
    
    

def get_config_dnsmasq(dhcprange):
    """
    Try to install dnsmasq (dhcp server) on host machine if not present
    in second step adjusts the address range

    :return: None
    :rtype: None
    """
    filename = "/usr/sbin/dnsmasq"

    if not os.path.isfile(filename):
        print("dhcp server (dnsmasq) not found, installing now...")
        os.system("apt-get install dnsmasq")

    if not os.path.isfile(filename):
        sys.exit(("\nUnable to install the \'dnsmasq\' package!\n" + 
                  "This process requires a persistent internet connection!\n" +
                  "Run apt-get update for changes to take effect.\n" +
                  "Rerun the script to install dnsmasq.\n" +
                  "Closing"))

    filename = "/usr/sbin/dnsmasq.conf"
    if(search(filename, "interface=wlan0") > 0):
        return
    else:
        body = "interface=wlp1s0b1\n%s\n" % (dhcprange)
        text_file = open(filename, "w")
        text_file.write(body)
        text_file.close()


def get_hostapd():
    """
    Try to install hostapd on host system if not present

    :return: None
    :rtype: None
    """
    filename = "/usr/sbin/hostapd"

    if not os.path.isfile(filename):
        print(filename + " not found, installing now...")
        os.system("apt-get install hostapd")

    if not os.path.isfile(filename):
        sys.exit(("\nUnable to install the \'hostapd\' package!\n" + 
        "This process requires a persistent internet connection!\n" +
        "Run apt-get update for changes to take effect.\n" +
        "Rerun the script to install hostapd.\n" +
        "Closing"))


def search(str, filename):
    if not os.path.isfile(filename):
        return -1
    n = 0
    with open(filename, 'r') as f:
        for line in f:
            if re.search(str, line):
                return n
            n += 1
    return -1
 

def configure_hostapd():
  filename = "/etc/hostapd/hostapd.conf"
  if not os.path.isfile(filename):
       print("hostapd (AP) not installed, go further without...")
       return
  ssid = input('Access point SSID: ')
  psk = input('Password: ')
  body = ("interface=wlan0\n" +
        "ssid=%s\n" +
        "hw_mode=g\n" +
        "channel=7\n" +
        "wmm_enabled=0\n" +
        "macaddr_acl=0\n" +
        "auth_algs=1\n" +
        "ignore_broadcast_ssid=0\n" +
        "wpa=2\n" +
        "wpa_passphrase=%s\n" +
        "wpa_key_mgmt=WPA-PSK\n" +
        "wpa_pairwise=TKIP\n" +
        "rsn_pairwise=CCMP\n" +
        "ctrl_interface=/var/run/hostapd\n" +
        "ctrl_interface_group=0\n") % (ssid, psk)
  text_file = open(filename, "w")
  text_file.write(body)
  text_file.close()

def make_reliable_init_hostapd(setupDir, IP):
    """
    RPI-tight integration using the kernel network driver
    
    :return: positive or 0 by success
    :rtype: The folder of installation and the ip address of the AP
    """
    filename = "/etc/init.d/hostapd"
    if not os.path.isfile(filename):
       print("hostapd (AP) not installed, go further without...")
       return 0

    os.chdir(setupDir)
    os.chdir("rocketlauncher")

    src_file = open("hostapd", "r") 
    body = src_file.read()
    src_file.close()
    body = body % (IP)
    text_file = open(filename, "w")
    text_file.write(body)
    text_file.close()
    
    print("hostapd (AP) reliably integrated ...")
    return 0
  
  
def adjust_http_docroot(setupDir, scriptname):
    """
    set up the default doc-root into Rocket doc-root
    
    :return: None
    :rtype: The folder of installation
    """

    filename = "/etc/daisy/config"
   
    if not os.path.isfile(filename):
       print("daisy not installed, exit...")
       return
   
    docroot = ("%s/rocket/html") % (setupDir)
    myscript = ("%s/rocket/python/%s") % (setupDir, scriptname)
    body = ("[GPIO]\n" +
        "[~GPIO]\n" +
        "[SCRIPTS]\n" +
        "myscript = %s\n" +
        "[HTTP]\n" +
        "enabled = true\n" +
        "port = 8000\n" +
        "doc-root = %s\n" +
        "passwd-file = /etc/daisy/passwd\n" +
        "prompt = \"Daisy\"\n" +
        "welcome-file = Index.html\n" +
        "[COAP]\n" +
        "enabled = true\n" +
        "port = 5683\n" +
        "multicast = true\n" +
        "[DEVICES]\n" +
        "[REST]\n" +
        "[ROUTES]\n") % (myscript, docroot)
    text_file = open(filename, "w")
    text_file.write(body)
    text_file.close()

    print("Rocket front end activated. Use http://192.168.4.1:8000")
    
def adjust_rocketlauncher(setupDir):
    """
    activates the RIB (if the binary is available) to be started at boot time
    
    :return: positive or 0 by success
    :rtype: The folder of installation
    """
    
    os.chdir(setupDir)
    os.chdir("rocketlauncher")
    filename = "/etc/systemd/system/rocket.service"

    src_file = open("rocket.service", "r") 
    body = src_file.read()
    src_file.close()
    

    if not os.path.isfile("RIB_App"):
       print("Installation done. Enjoy the demonstration project maxmotion.")
       body = body % (setupDir + "/rocketlauncher/rocketlauncher.sh", setupDir + "/rocketlauncher")
       text_file = open(filename, "w")
       text_file.write(body)
       text_file.close()
    
       print("Installation of the the demonstration project maxmotion is done. Enjoy, motion launches at start ...")
       return -1


    body = body % (setupDir + "/rocketlauncher/rocketlauncherS.sh", setupDir + "/rocketlauncher")
    text_file = open(filename, "w")
    text_file.write(body)
    text_file.close()
    
    print("Installation done. Enjoy. RIB and Co. launches at start ...")
    return 0

def get_maxmotion_lib(setupDir):
    """
    takes the git repo for the maxmotion project
    takes the spidev and pydev modules
    builds the project
    
    :return: positive or 0 by success
    :rtype: The folder of installation
    """
    
    os.chdir(setupDir)
    
    repo = "maxmotion"
    if os.path.isdir(repo):
       print("Nothing to clone. %s already here." % (repo))
       return -1

    os.system("git clone https://github.com/gulliversoft/%s" % (repo))
    
    if not os.path.isdir(repo):
        print("The example could not be build. Missing %s repo " %(repo))
        return -1
    
    os.chdir(repo)
    #installs Python C-API
    os.system("apt-get install python-dev")
    #install module for interfacing with SPI devices from user space via the spidev linux kernel driver
    os.system("pip3 install spidev")
    
    os.system("python3 setup.py install")
    
    print("Installation done. Enjoy the demonstration project %s." % (repo))
    return 0

def install_daisy(setupDir):
    """
    instal python modules around of daisy   
    :return: positive or 0 by success
    :rtype: The folder of installation
    """
    
    os.chdir(setupDir)
    os.chdir("daisy")
    os.system("bash ./daisy_setup.sh")
    
    print("Installation done. Enjoy Daisy ...")
    return 0
    
    
    
