from sqlalchemy import Column, Integer, String
from backend.database.database import Base


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    goal = Column(String, nullable=False)

    skills = Column(String, nullable=False)

    daily_hours = Column(Integer, nullable=False)