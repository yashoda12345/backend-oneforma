from typing import List
from pydantic import BaseModel


class SkillMapperCreate(BaseModel):
    skill: List[int]

    class Config:
        orm_mode = True
