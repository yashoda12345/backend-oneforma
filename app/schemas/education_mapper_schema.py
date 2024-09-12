from pydantic import BaseModel


class EducationMapperCreate(BaseModel):
    degree: int
    field_of_study: str

    class Config:
        orm_mode = True
