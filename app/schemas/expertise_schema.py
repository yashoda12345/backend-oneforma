from pydantic import BaseModel


class ExpertiseCreateBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class ExpertiseResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
