import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_HOST = os.getenv("API_HOST_BIND_IP", "127.0.0.1")
API_PORT = int(os.getenv("API_HOST_PORT", "8080"))

def test_api_bind_to_correct_host_and_port():
    with httpx.Client() as client:
        response = client.get(f"http://{API_HOST}:{API_PORT}/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, World!"}