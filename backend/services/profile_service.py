from sqlalchemy.orm import Session

from backend.models.user import User
from backend.database.models import UserDB


def save_profile(user: User, db: Session):

    db_user = UserDB(
        name=user.name,
        goal=user.goal,
        skills=",".join(user.skills),
        daily_hours=user.daily_hours
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_profile(db: Session):

    return db.query(UserDB).order_by(UserDB.id.desc()).first()