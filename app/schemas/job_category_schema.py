from pydantic import BaseModel


class JobCategoryBase(BaseModel):
    name: str

    class Config:
        orm_mode = True
