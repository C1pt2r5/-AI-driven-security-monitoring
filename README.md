# -AI-driven-security-monitoring

## Overview
The **Network Anomaly Detection System** is an AI-powered tool designed to monitor network traffic, detect anomalies in real-time, and provide a web dashboard for visualization. The system leverages **machine learning (Isolation Forest)** for anomaly detection and integrates **Flask** for web-based reporting.

## Features
- **Real-time Packet Monitoring:** Captures network packets using `scapy`.
- **Anomaly Detection:** Uses Isolation Forest to identify abnormal packet lengths.
- **Database Logging:** Stores network traffic data in an SQLite database.
- **Web Dashboard:** Displays real-time traffic data and anomaly analysis using Flask.
- **Data Visualization:** Generates network traffic plots for better analysis.

## Project Structure
```
├── anomaly_detector.py      # ML model for anomaly detection
├── database_setup.py        # SQLite database setup
├── network_monitor.py       # Packet sniffer and logger
├── web_dashboard.py         # Flask-based web dashboard
├── templates/
│   ├── index.html          # Web dashboard template
├── static/
│   ├── styles.css          # Dashboard styling (if applicable)
├── README.md               # Documentation
```

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- SQLite
- Required Python libraries (install using the command below)

```sh
pip install scapy flask numpy scikit-learn matplotlib
```

### Step 1: Setup Database
Run the following command to initialize the database:
```sh
python database_setup.py
```

### Step 2: Start Network Monitoring
Execute the network monitoring script:
```sh
sudo python network_monitor.py
```
(Note: `sudo` may be required to capture packets.)

### Step 3: Launch Web Dashboard
Run the Flask web application:
```sh
python web_dashboard.py
```
Access the dashboard at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## How It Works
1. **Packet Capture:** `network_monitor.py` captures network packets using `scapy`.
2. **Anomaly Detection:** The captured packets are analyzed by `anomaly_detector.py` using Isolation Forest.
3. **Database Logging:** All packets (normal & anomalous) are stored in `network_logs.db`.
4. **Web Dashboard:** `web_dashboard.py` fetches logs and visualizes traffic data.

## Future Enhancements
- Improve anomaly detection using more ML techniques.
- Support additional network protocols.
- Enhance web dashboard with real-time graphs.
- Deploy on cloud for distributed monitoring.

## License
This project is open-source and available under the **Apache Server**.

