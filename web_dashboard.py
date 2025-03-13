from flask import Flask, render_template, jsonify
import sqlite3
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Fetch logs from the database
def fetch_logs():
    conn = sqlite3.connect("logs/network_logs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM packets ORDER BY timestamp DESC")
    data = cursor.fetchall()
    conn.close()
    return data

# Route: Home page
@app.route("/")
def index():
    logs = fetch_logs()
    return render_template("index.html", logs=logs)

# Route: Get data in JSON format
@app.route("/get_data")
def get_data():
    logs = fetch_logs()
    return jsonify(logs)

# Route: Generate network traffic graph
@app.route("/plot")
def plot():
    conn = sqlite3.connect("logs/network_logs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, length FROM packets ORDER BY timestamp DESC")
    data = cursor.fetchall()
    conn.close()
    
    if not data:
        return "No data available for visualization."

    timestamps, lengths = zip(*data)
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, lengths, marker="o", linestyle="-", color="b")
    plt.xlabel("Timestamp")
    plt.ylabel("Packet Length")
    plt.title("Network Traffic Analysis")
    plt.xticks(rotation=45)
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return f'<img src="data:image/png;base64,{graph_url}"/>'

if __name__ == "__main__":
    app.run(debug=True)
