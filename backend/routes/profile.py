from fastapi import APIRouter
from backend.models.user import User
from backend.services.profile_service import (
    save_profile,
    get_profile
)

router = APIRouter()


@router.post("/profile")
def create_profile(user: User):

    profile = save_profile(user)

    return {
        "message": "Profile created successfully!",
        "user": profile
    }


@router.get("/profile")
def read_profile():

    profile = get_profile()

    if profile is None:
        return {
            "message": "No profile found."
        }

    return profile