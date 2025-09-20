import os
import time
import threading
from dotenv import load_dotenv

import pytest
import uvicorn
import httpx

load_dotenv()

API_HOST = os.getenv("API_HOST_BIND_IP", "127.0.0.1")
API_PORT = int(os.getenv("API_HOST_PORT", "8080"))

def run_server():
    uvicorn.run("api.main:app", host=API_HOST, port=API_PORT)

@pytest.fixture(scope="session", autouse=True)
def start_server():
    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()
    
    # Wait for server to be ready by polling health endpoint
    max_attempts = 10
    attempt = 0
    while attempt < max_attempts:
        try:
            response = httpx.get(f"http://{API_HOST}:{API_PORT}/health", timeout=1.0)
            if response.status_code == 200:
                break
        except httpx.RequestError:
            pass
        time.sleep(0.5)
        attempt += 1
    else:
        raise RuntimeError("Server did not start within expected time")