from pydantic import BaseModel


class IntrestCreateBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class IntrestResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
