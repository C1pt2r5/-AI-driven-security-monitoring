import sqlite3

def setup_database():
    conn = sqlite3.connect("logs/network_logs.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS packets (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        src_ip TEXT,
                        dest_ip TEXT,
                        protocol TEXT,
                        length INTEGER,
                        anomaly INTEGER DEFAULT 0)''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    setup_database()
