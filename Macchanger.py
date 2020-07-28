#!/usr/bin/env python

import subprocess


print('''  Author:Ashwath Mittal
         * Legall Disclaimer: Developers or anyone associated with this Repository assume no liablity
           and they are not responsible for how you use this tool.Please use this tool for educational purpose only.* ''' )
interface = raw_input("Please sepcify the interface:")
new_mac = raw_input("Pleae specify new mac:")

print("[!] Changing MAC ADDRESS for " + interface + " to " + new_mac )
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
