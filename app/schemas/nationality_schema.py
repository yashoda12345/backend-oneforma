from pydantic import BaseModel


class NationalityCreateBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class NationalityResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
