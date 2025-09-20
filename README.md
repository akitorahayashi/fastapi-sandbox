# FastAPI Sandbox

A minimal FastAPI sandbox environment.

## Overview

- **FastAPI**: Modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Setup

1. **Setup environment**:
   ```bash
   just setup
   ```
   This will create `.env` file from `.env.example` if it doesn't exist and install dependencies with `uv sync`.

## How to Run

1. **Start FastAPI server**:
   ```bash
   uv run uvicorn api.main:app --reload
   ```

2. **Using Docker Compose**:
   ```bash
   just dev
   ```
   This will start the FastAPI server in a container.

## API Usage Examples

Once the server is running, you can test the basic endpoints.

### Basic Endpoints
- **Root**: GET `/`
  - Response: `{"message": "Welcome to FastAPI Sandbox"}`

- **Health Check**: GET `/health`
  - Response: `{"status": "healthy"}`

- **Get Item**: GET `/items/{item_id}?q=query`
  - Response: `{"item_id": 123, "q": "query"}`

### Example Usage
```bash
# Root endpoint
curl "http://localhost:8080/"

# Health check
curl "http://localhost:8080/health"

# Get item
curl "http://localhost:8080/items/123?q=test"
```

## For Developers

- `justfile`: For convenient task execution
  - `just setup`: Setup environment and install dependencies
  - `just dev`: Start the service with Docker Compose
  - `just stop`: Stop all services
- `Dockerfile`: For containerization
- `docker-compose.yml`: For environment setup

## Project Structure

```
fastapi-sandbox/
├── api/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   └── Dockerfile       # API container
├── tests/
│   └── e2e/             # End-to-end tests
├── docker-compose.yml   # Docker services
├── justfile             # Task runner
├── pyproject.toml       # Project configuration
└── README.md            # This file
```
