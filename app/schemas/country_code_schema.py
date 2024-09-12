from pydantic import BaseModel


class CountryCodeCreateBase(BaseModel):
    name: str
    country: int

    class Config:
        orm_mode = True


class CountryCodeResponse(BaseModel):
    id: int
    code: int

    class Config:
        orm_mode = True
