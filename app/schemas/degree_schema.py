from pydantic import BaseModel


class DegreeCreateBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class DegreeResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
