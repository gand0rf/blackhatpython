#!/usr/bin/env python

from scapy.all import sniff

def packet_callback(packet):
    #print(packet.show())
    #if "Ethernet" in packet:
    #    print(packet["Ethernet"].type)
    #if "IP" in packet:
    #    print(packet["IP"].proto)
    if "IP" in packet and packet["IP"].proto == 6:
        print(packet)

def main():
    sniff(prn=packet_callback, count=1)

if __name__ == "__main__":
    main()
