import sqlite3
import numpy as np
from sklearn.ensemble import IsolationForest

# Train Isolation Forest model
def train_model():
    conn = sqlite3.connect("logs/network_logs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT length FROM packets ORDER BY timestamp DESC LIMIT 1000")
    data = cursor.fetchall()
    conn.close()

    if not data:
        return None

    X = np.array([x[0] for x in data]).reshape(-1, 1)

    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X)
    return model

# Detect if a packet is an anomaly
def detect_anomaly(packet_length):
    model = train_model()
    if model is None:
        return 0  # No model trained yet, assume normal

    prediction = model.predict([[packet_length]])
    return 1 if prediction[0] == -1 else 0  # 1 for anomaly, 0 for normal
