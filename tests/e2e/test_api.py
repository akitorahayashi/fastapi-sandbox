import httpx


class TestAPISandboxE2E:
    """Basic tests for FastAPI sandbox."""

    def test_health_endpoint(self, api_base_url):
        """Test health check endpoint."""
        response = httpx.get(f"{api_base_url}/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
