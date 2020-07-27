#!/usr/bin/env python

import subprocess

print(''' |\   /\  /|
          | \ /  \/ |     Author:Ashwath Mittal
          |  \/   /\|
          | / \  /  \|
          |/   \/    |\
                                        ''' )
interface = raw_input("Interface:")
new_mac = raw_input("Please enter new mac:")

subprocess.call("ifconfig" + interface + "down", shell=True)
subprocess.call("ifconfig" + interface + "hw ether" + new_mac, shell=True)
subprocess.call("ifconfig" + interface + "up", shell=True)

print("changing mac for" + interface +"to" + new_mac)

subprocess.call("ifconfig" + interface, shell=True)
