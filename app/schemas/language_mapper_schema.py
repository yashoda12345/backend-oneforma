from pydantic import BaseModel
from typing import List


class LanguageMapperCreateBase(BaseModel):
    spoken_language: int
    proficiency: int

    class Config:
        orm_mode = True


class LanguageMapperResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
