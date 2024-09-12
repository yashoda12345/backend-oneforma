from typing import Optional
from pydantic import BaseModel
from .user_schema import UserInDBBase


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserInDBBase


class TokenPayload(BaseModel):
    sub: Optional[int] = None
