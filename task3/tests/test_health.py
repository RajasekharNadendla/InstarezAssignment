import requests
from multiprocessing import Process
import time
import app

def run_app():
    app.app.run(host="0.0.0.0", port=5001)

def test_health_endpoint():
    # run flask app in a separate process using port 5001
    p = Process(target=run_app, daemon=True)
    p.start()
    time.sleep(1.0)
    r = requests.get("http://127.0.0.1:5001/health", timeout=5)
    assert r.status_code == 200
    assert r.json().get("status") == "healthy"
    p.terminate()
