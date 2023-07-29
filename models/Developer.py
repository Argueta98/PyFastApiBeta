from pydantic import BaseModel
from typing import List
from models.Skill import Skill
from models.Language import Language

class Developer(BaseModel):
    _id: str
    name: str
    age: int
    address: str
    skills: List[Skill]
    langaueg: List[Language]