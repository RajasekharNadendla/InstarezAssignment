from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "backend healthy"})

@app.route("/hello")
def hello():
    return jsonify({"msg":"hello from backend"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
