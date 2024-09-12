from pydantic import BaseModel


class SkillCreateBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class SkillResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
