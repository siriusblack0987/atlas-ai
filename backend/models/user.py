from pydantic import BaseModel

class User(BaseModel):
    name: str
    goal: str
    skills: list[str]
    daily_hours: int

