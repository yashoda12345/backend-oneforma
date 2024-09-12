from pydantic import BaseModel


class GenderCreateBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class GenderResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
