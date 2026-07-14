from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.services.profile_service import get_profile
from backend.services.gap_analysis_service import analyze_gap
from backend.services.project_service import recommend_projects

router = APIRouter()


@router.get("/analyze")
def analyze(db: Session = Depends(get_db)):

    profile = get_profile(db)

    if profile is None:
        return {
            "message": "No profile found."
        }

    skills = profile.skills.split(",")

    report = analyze_gap(
        profile.goal,
        skills
    )

    if "error" in report:
        return report

    projects = recommend_projects(
        report["missing_skills"]
    )

    report["recommended_projects"] = projects

    return report