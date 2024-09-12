from pydantic import BaseModel


class StateCreateBase(BaseModel):
    name: str
    country_code: int

    class Config:
        orm_mode = True


class StateResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
