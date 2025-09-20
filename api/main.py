from fastapi import FastAPI

app = FastAPI(
    title="fastapi-sandbox", description="A minimal FastAPI sandbox environment."
)


@app.get("/")
def hello():
    """Hello endpoint."""
    return {"message": "Hello, World!"}


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
