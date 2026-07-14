from fastapi import FastAPI

from backend.routes.profile import router as profile_router
from backend.routes.resume import router as resume_router

from backend.database.database import Base, engine
from backend.database import models
from backend.routes.analyze import router as analyze_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Atlas AI",
    description="An AI mentor for aspiring software engineers.",
    version="0.1.0"
)

# Include routes
app.include_router(profile_router)
app.include_router(resume_router)
app.include_router(analyze_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Atlas AI!",
        "status": "Backend is running successfully 🚀"
    }