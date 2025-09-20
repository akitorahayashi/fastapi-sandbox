import requests
import pytest


class TestAPISandbox:
    """Basic tests for FastAPI sandbox."""

    def test_health_endpoint(self, base_url):
        """Test health check endpoint."""
        response = requests.get(f"{base_url}/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"