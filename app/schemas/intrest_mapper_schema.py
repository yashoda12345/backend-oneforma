from typing import List
from pydantic import BaseModel


class IntrestMapperCreate(BaseModel):
    intrest: List[int]

    class Config:
        orm_mode = True
