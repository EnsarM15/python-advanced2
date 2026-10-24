from pydantic import BaseModel
from typing import Optional

class Developer(BaseModel):
    name: str
    experience: Optional[int] = None


class Project(BaseModel):
    title: str
    description: Optional[str] = None
    languages: Optional[list[str]] = []

    lead_developer: Developer