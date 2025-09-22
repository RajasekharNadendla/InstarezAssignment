import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

DB_NAME = os.environ.get("POSTGRES_DB")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_HOST = os.environ.get("DB_HOST", "db")

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/db-test')
def db_test():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        conn.close()
        return jsonify({"status": "database connection successful"})
    except Exception as e:
        return jsonify({"status": f"database connection failed: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)