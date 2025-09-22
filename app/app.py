from flask import Flask, jsonify
import os
import psycopg2
import psycopg2.extras
from psycopg2 import OperationalError

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/db-test")
def db_test():
    db_host = os.getenv("POSTGRES_HOST", "db")
    db_port = int(os.getenv("POSTGRES_PORT", 5432))
    db_name = os.getenv("POSTGRES_DB", "appdb")
    db_user = os.getenv("POSTGRES_USER", "admin")
    db_pass = os.getenv("POSTGRES_PASSWORD", "password123")

    try:
        conn = psycopg2.connect(host=db_host, port=db_port, dbname=db_name,
                                user=db_user, password=db_pass, connect_timeout=5)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT 1;")
        cur.close()
        conn.close()
        return jsonify({"db": "ok"}), 200
    except OperationalError as e:
        # include message for debugging
        return jsonify({"db": "error", "msg": str(e)}), 500

if __name__ == "__main__":
    # Flask runs on 0.0.0.0:5000 inside container
    app.run(host="0.0.0.0", port=5000)
