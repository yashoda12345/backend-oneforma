from pydantic import BaseModel


class LanguageCreateBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class LanguageResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
