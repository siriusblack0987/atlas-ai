from fastapi import APIRouter, UploadFile, File

from backend.services.resume_service import save_resume

router = APIRouter()


@router.post("/resume")
def upload_resume(file: UploadFile = File(...)):

    result = save_resume(file)

    return {
        "message": "Resume uploaded successfully!",
        "filename": file.filename,
        "saved_to": result["path"],
        "skills": result["skills"]
    }