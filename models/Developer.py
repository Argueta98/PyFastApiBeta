from pydantic import BaseModel
from typing import List
from models.Skill import Skill
from models.Language import Lenguage

class Developer(BaseModel):
    _id: str
    name: str
    age: int
    address: str
    skills: List[Skill]
    language: List[Lenguage]