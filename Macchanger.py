#!/usr/bin/env python

import subprocess

print(''' Author:Ashwath Mittal
           ## Legall Disclaimer: Developers or anyone associated with this Repository assume no liablity                                                  
           and they are not responsible for how you use this tool.Please use this tool for educational purpose only. ''' )

Interface = raw_input("Please enter the Interface:")
new_mac = raw_input("Please enter new mac:")

subprocess.call("ifconfig " + Interface + " down", shell=True)
subprocess.call("ifconfig " + Interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig "+ Interface + " up", shell=True)

print("Your Mac is changed")

