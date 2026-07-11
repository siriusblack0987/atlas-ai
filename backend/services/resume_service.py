from backend.utils.pdf_parser import extract_text
from backend.utils.skill_extractor import extract_skills
import os
import shutil

UPLOAD_FOLDER = "uploads"


def save_resume(file):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)

    skills = extract_skills(text)

    return {
    "path": file_path,
    "text": text,
    "skills": skills
}