from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI(
    title="Atlas AI",
    description="An AI mentor for aspiring software engineers.",
    version="0.1.0"
)

# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Atlas AI!",
        "status": "Backend is running successfully 🚀"
    }