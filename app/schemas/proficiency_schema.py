from pydantic import BaseModel


class ProficiencyCreateBase(BaseModel):
    level: str

    class Config:
        orm_mode = True


class ProficiencyResponse(BaseModel):
    id: int
    level: str

    class Config:
        orm_mode = True
