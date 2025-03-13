from scapy.all import sniff
import sqlite3
from anomaly_detector import detect_anomaly

# Function to store packet details in the database
def log_packet(src_ip, dest_ip, protocol, length, anomaly):
    conn = sqlite3.connect("logs/network_logs.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO packets (src_ip, dest_ip, protocol, length, anomaly) VALUES (?, ?, ?, ?, ?)",
                   (src_ip, dest_ip, protocol, length, anomaly))
    
    conn.commit()
    conn.close()

# Callback function to process each captured packet
def process_packet(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dest_ip = packet["IP"].dst
        protocol = packet["IP"].proto
        length = len(packet)
        
        anomaly = detect_anomaly(length)
        
        print(f"Captured: {src_ip} -> {dest_ip} | Protocol: {protocol} | Length: {length} | Anomaly: {anomaly}")
        log_packet(src_ip, dest_ip, protocol, length, anomaly)

# Start sniffing packets
def start_sniffing():
    print("Starting packet capture...")
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    start_sniffing()
