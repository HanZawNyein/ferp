from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from db.crud import CRUDBase
from .models import Group
from .schemas import GroupCreate, GroupUpdate


class CRUDItem(CRUDBase[Group, GroupCreate, GroupUpdate]):
    ...


group = CRUDItem(Group)
