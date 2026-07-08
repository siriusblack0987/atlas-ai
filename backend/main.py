from fastapi import FastAPI
from backend.routes.profile import router as profile_router

app = FastAPI(
    title="Atlas AI",
    description="An AI mentor for aspiring software engineers.",
    version="0.1.0"
)

# Include profile routes
app.include_router(profile_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Atlas AI!",
        "status": "Backend is running successfully 🚀"
    }