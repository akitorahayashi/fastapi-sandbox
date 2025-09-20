import os
import pytest
from dotenv import load_dotenv

load_dotenv('.env')

@pytest.fixture(scope="session")
def api_host_bind_ip():
    return os.getenv('API_HOST_BIND_IP', '127.0.0.1')

@pytest.fixture(scope="session")
def api_test_port():
    return os.getenv('API_TEST_PORT', '8081')

@pytest.fixture(scope="session")
def base_url(api_host_bind_ip, api_test_port):
    """Base URL for the API."""
    return f"http://{api_host_bind_ip}:{api_test_port}"