from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str
    email: Optional[str]


class UserCreate(UserBase):
    ...


class UserUpdate(BaseModel):
    username: Optional[str]
    password: Optional[str]
    email: Optional[str]


class UserInDBBase(UserBase):
    id: int

    class ConfigDict:
        from_attributes = True


class Group(UserInDBBase):
    pass


class GroupInDB(UserInDBBase):
    pass
