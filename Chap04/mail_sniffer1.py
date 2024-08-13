from scapy.all import sniff, Ether

def packet_callback(packet):
    if 'IP' in packet:
        if packet['IP'].src != '192.168.50.99' and packet['IP'].dst != '192.168.50.99' and packet['IP'].proto != 2 and 'UDP' not in packet: #2 == igmp
            print( packet)
    elif 'Ether' in packet:
        if packet['Ethernet'].type != 2054 and packet['Ethernet'].type != 35020: #2054 == ARP, 35020 == LLDP
            print(packet)

def main():
    sniff(prn=packet_callback, count=1000)


if __name__ == '__main__':
    main()
