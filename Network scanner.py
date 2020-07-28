#!/usr/bin/env python

import scapy.all as scapy

ipf =raw_input("Please secify the gateway(run route -n):")
def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff:ff")
    arp_request_brd = broadcast/arp_request
    answered_list = scapy.srp(arp_request_brd, timeout=1, verbose=False)[0]

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(result_list):
    print("IP\t\tMAC address\n---------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

scan_result=scan(ipf/24)
print_result(scan_result)
