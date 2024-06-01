from scapy.all import *

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        
        print("\n[+] New Packet Captured:")
        print(f"    Source IP: {src_ip} --> Destination IP: {dst_ip}")
        print(f"    Protocol: {protocol}")

        # Extracting additional information based on the protocol
        if protocol == 6 and TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            payload = packet[TCP].payload
            print(f"    Source Port: {src_port} --> Destination Port: {dst_port}")
            print(f"    Payload: {payload}")
        elif protocol == 17 and UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            payload = packet[UDP].payload
            print(f"    Source Port: {src_port} --> Destination Port: {dst_port}")
            print(f"    Payload: {payload}")

def start_sniffing(interface, filter=None):
    print(f"[*] Sniffing started on interface: {interface}")
    if filter:
        print(f"[*] Filtering packets for destination IP: {filter}")
    sniff(iface=interface, filter=filter, prn=packet_callback, store=0)

if __name__ == "__main__":
    interface = input("Enter the network interface to sniff (e.g., eth0, wlan0): ")
    filter_ip = input("Enter destination IP to filter (leave blank for all): ")

    if filter_ip:
        filter_str = f"dst {filter_ip}"
    else:
        filter_str = None

    start_sniffing(interface, filter_str)
