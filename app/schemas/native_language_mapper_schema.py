from pydantic import BaseModel


class NativeLanguageCreateBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class NativeLanguageResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
