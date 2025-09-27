# app/app.py
import os
import json
from flask import Flask, jsonify
import psycopg2
from psycopg2 import sql, OperationalError

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("POSTGRES_DB", "appdb")
DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "password123")
DB_PORT = os.getenv("DB_PORT", "5432")

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/db-test")
def db_test():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT, connect_timeout=5
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        if result and result[0] == 1:
            return jsonify({"db": "ok"}), 200
        else:
            return jsonify({"db": "unexpected result", "result": result}), 500
    except Exception as e:
        return jsonify({"db": "error", "error": str(e)}), 500

if __name__ == "__main__":
    # Flask should run on port 5000 inside container
    app.run(host="0.0.0.0", port=5000)
