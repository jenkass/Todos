from pydantic import BaseModel, EmailStr
from typing import List, Optional

from models.events import Event


class User(BaseModel):
    id: int
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Event]]


class UserSignIn(BaseModel):
    email: EmailStr
    password: str
