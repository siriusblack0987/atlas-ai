from fastapi import FastAPI
from backend.models.user import User
# Create the FastAPI application
app = FastAPI(
    title="Atlas AI",
    description="An AI mentor for aspiring software engineers.",
    version="0.1.0"
)
current_user = None

# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Atlas AI!",
        "status": "Backend is running successfully 🚀"
    }


@app.post("/profile")
def create_profile(user: User):

    global current_user

    current_user = user

    return {
        "message": "Profile created successfully!",
        "user": current_user
    }

@app.get("/profile")
def get_profile():

    if current_user is None:
        return {
            "message": "No profile found."
        }

    return current_user