from pydantic import BaseModel


class Lenguage(BaseModel):
    name: str
    level: int
