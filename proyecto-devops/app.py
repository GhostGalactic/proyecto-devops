from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Proyecto DevOps en la Nube</h1><p>Aplicación desplegada con Docker y Kubernetes.</p>"

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/api/status")
def status():
    return jsonify({
        "service": "devops-app",
        "version": "1.0.0",
        "environment": "cloud"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)