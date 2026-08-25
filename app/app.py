from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "application": "Contoso DevSecOps Platform",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "status": "healthy"
    }

@app.route("/health")
def health():
    return {
        "status": "healthy"
    }

@app.route("/ready")
def ready():
    return {
        "status": "ready"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
