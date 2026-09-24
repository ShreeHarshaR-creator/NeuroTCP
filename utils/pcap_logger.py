from scapy.all import IP, TCP, wrpcap
import os

def generate_pcap_trace(telemetry_data, output_path, src_ip="192.168.1.100", dst_ip="8.8.8.8"):
    """
    Reads the JSON telemetry (sent, processed, dropped) and generates 
    a realistic PCAP file that can be opened in Wireshark.
    """
    packets = []
    
    print(f"Generating PCAP trace for Wireshark at {output_path}...")
    
    for entry in telemetry_data:
        # Simulate successful packets (ACKs)
        for _ in range(int(entry["processed"])):
            pkt = IP(src=src_ip, dst=dst_ip)/TCP(sport=12345, dport=443, flags="A")
            packets.append(pkt)
            
        # Simulate dropped packets (Retransmissions/Resets)
        for _ in range(int(entry["dropped"])):
            pkt = IP(src=src_ip, dst=dst_ip)/TCP(sport=12345, dport=443, flags="R")
            packets.append(pkt)
            
    # Write to file
    wrpcap(output_path, packets)
    print("PCAP generation complete.")
