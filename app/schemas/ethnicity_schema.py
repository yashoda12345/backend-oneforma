from pydantic import BaseModel


class EthnicityCreateBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class EthnicityResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
