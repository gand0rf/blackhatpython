import socket
import os

def main(HOST, pt):
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    elif pt == '1':
        socket_protocol = socket.IPPROTO_ICMP
    elif pt == '2':
        socket_protocol = socket.IPPROTO_TCP
    elif pt == '3':
        socket_protocol = socket.IPPROTO_UDP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    while True:    
        print(sniffer.recvfrom(65565))

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    

if __name__ == '__main__':
    HOST = str(os.popen("ifconfig eno1 | awk '/inet / {print $2}'").read()).strip()
    packet_type = input('1)ICMP 2)TCP 3)UDP: ')
    print(f'Listening on {HOST}....')
    main(HOST, packet_type)
