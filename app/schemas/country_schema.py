from pydantic import BaseModel


class CountryCreateBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CountryResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
