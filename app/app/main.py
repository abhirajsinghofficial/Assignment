from fastapi import FastAPI, Request
from datetime import datetime, timezone

app = FastAPI()

@app.get("/")
async def root(request: Request):
    """
    Returns current UTC timestamp and client IP address.
    """
    client_ip = request.client.host if request.client else "unknown"

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "ip": client_ip
    }
