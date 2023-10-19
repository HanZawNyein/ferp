from typing import Optional

from pydantic import BaseModel


# Shared properties
class GroupBase(BaseModel):
    name: Optional[str] = None


class GroupCreate(GroupBase):
    ...


class GroupUpdate(GroupBase):
    ...


class GroupInDBBase(GroupBase):
    id: int
    name:str

    class Config:
        from_attributes = True


# Properties to return to client
class Group(GroupInDBBase):
    pass


# Properties properties stored in DB
class GroupInDB(GroupInDBBase):
    pass
