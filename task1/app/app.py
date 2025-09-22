from flask import Flask, jsonify
import os
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)

DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = int(os.getenv("POSTGRES_PORT", 5432))
DB_NAME = os.getenv("POSTGRES_DB", "appdb")
DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "password123")

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/db-test")
def db_test():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            connect_timeout=5
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"db": "ok"})
    except OperationalError as e:
        return jsonify({"db": "error", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

