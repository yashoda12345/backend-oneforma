from pydantic import BaseModel


class IndustryCreateBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class IndustryResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
