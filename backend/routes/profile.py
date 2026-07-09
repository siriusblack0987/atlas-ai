from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.models.user import User
from backend.database.database import get_db
from backend.services.profile_service import (
    save_profile,
    get_profile
)

router = APIRouter()


@router.post("/profile")
def create_profile(
    user: User,
    db: Session = Depends(get_db)
):
    profile = save_profile(user, db)

    return {
        "message": "Profile created successfully!",
        "user_id": profile.id
    }


@router.get("/profile")
def read_profile(
    db: Session = Depends(get_db)
):
    profile = get_profile(db)

    if profile is None:
        return {
            "message": "No profile found."
        }

    return {
        "id": profile.id,
        "name": profile.name,
        "goal": profile.goal,
        "skills": profile.skills.split(","),
        "daily_hours": profile.daily_hours
    }