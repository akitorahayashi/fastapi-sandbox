# FastAPI Sandbox

A minimal FastAPI sandbox environment.

## Project Structure

```
fastapi-sandbox/
├── .github/workflows/run-tests.yml
├── api/
│   ├── __init__.py
│   ├── main.py
│   └── Dockerfile
├── tests/
│   ├── conftest.py
│   ├── e2e/             
│   ├── intg/            
│   └── unit/            
├── docker-compose.dev.yml
├── docker-compose.test.override.yml
├── .env.example
├── justfile
├── pyproject.toml
└── README.md
```

## Overview

A minimal FastAPI sandbox environment.

## Setup

1. **Setup environment**:
   ```bash
   just setup
   ```
   This will create `.env` file from `.env.example` if it doesn't exist and install dependencies with `uv sync`.

## How to Run

1. **Using just dev**:
   ```bash
   just dev
   ```
   This will start the FastAPI server with uvicorn in reload mode.

2. **Using just up**:
   ```bash
   just up
   ```
   This will start the service with Docker Compose.

## API Usage Examples

Once the server is running, you can test the basic endpoints.

### Basic Endpoints
- **Root**: GET `/`
  - Response: `{"message": "Welcome to FastAPI Sandbox"}`

- **Health Check**: GET `/health`
  - Response: `{"status": "healthy"}`

### Example Usage
```bash
# Root endpoint
curl -X GET "http://localhost:8080/" -H "accept: application/json"
# Expected response: {"message": "Welcome to FastAPI Sandbox"}

# Health check
curl -X GET "http://localhost:8080/health" -H "accept: application/json"
# Expected response: {"status": "healthy"}
```
