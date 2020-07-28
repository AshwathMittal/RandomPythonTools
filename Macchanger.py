#!/usr/bin/env python

import subprocess
import optparse
import re

print('''  Author:Ashwath Mittal
         * Legall Disclaimer: Developers or anyone associated with this Repository assume no liablity
           and they are not responsible for how you use this tool.Please use this tool for educational purpose only.* ''' )
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC ADDRESS")
    parser.add_option("-m", "--mac", dest="new_mac", help="Your new MAC ADDRESS")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[!] Please specify an interface, use --help for more info")
    elif not option.new_mac:
        parser.error("[!] Please specify an MAC, use --help for more info")
    return options
def mac_chng(interface, new_mac):
    print("[!] Changing MAC ADDRESS for " + Interface + " to " + new_mac)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)


options = get_arguments()
mac_chng(options.interface, options.new_mac)
