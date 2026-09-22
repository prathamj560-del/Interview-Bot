from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from limiter import limiter

# Load environment variables at startup
load_dotenv()

# Validate all required environment variables
from validate_env import validate_env_vars
validate_env_vars()

from routers.bot import bot_router
from routers.main_router import router as main_router
from routers.auth import auth_router
from routers.mock import mock_router
from routers.dashboard import dashboard_router

app = FastAPI()


# Use the shared limiter so app.state.limiter and all @limiter.limit()
# decorators in every router reference the exact same object.

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

def _get_cors_origins() -> list:
    """Read CORS_ORIGINS env var (comma-separated); fall back to localhost defaults."""
    import os
    raw = os.getenv("CORS_ORIGINS", "http://localhost:5173,http://localhost:3000")
    return [origin.strip() for origin in raw.split(",") if origin.strip()]


app.add_middleware(
    CORSMiddleware,
    allow_origins=_get_cors_origins(),
    allow_origin_regex=r"https://[a-z0-9-]+\.vercel\.app",  # any Vercel deployment/preview URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

app.include_router(bot_router)
app.include_router(main_router)
app.include_router(auth_router)
app.include_router(mock_router)
app.include_router(dashboard_router)

@app.get("/")
@limiter.limit("10/minute")
def home(request: Request):
    return {"hello": "world"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
