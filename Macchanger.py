#!/usr/bin/env python

import subprocess

print(''' Author:Ashwath Mittal
           ## Legall Disclaimer Developers or anyone associated with this Repository assume no liablity                                                  
           and they are not responsible for how you use this tool.Please use this tool for educational purpose only. ''' )


new_mac = raw_input("Please enter new mac:")

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether " + new_mac, shell=True)
subprocess.call("ifconfig eth0 up", shell=True)

print("Your Mac is changed")
