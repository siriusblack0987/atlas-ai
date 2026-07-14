from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.services.resume_service import save_resume
from backend.services.profile_service import update_skills

router = APIRouter()


@router.post("/resume")
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    result = save_resume(file)

    update_skills(
        db=db,
        skills=result["skills"]
    )

    return {
        "message": "Resume uploaded successfully!",
        "filename": file.filename,
        "saved_to": result["path"],
        "skills": result["skills"]
    }