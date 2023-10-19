from typing import List, Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from users.deps import get_db

# from .schemas import Group,GroupUpdate
from . import schemas
from .crud import group as crud_group

router = APIRouter()


@router.get('/groups', response_model=List[schemas.Group])
def read_groups(db: Session = Depends(get_db),
                skip: int = 0,
                limit: int = 100) -> Any:
    """
        Retrieve Groups.
        """
    return crud_group.get_multi(db=db, skip=skip, limit=limit)


@router.post('/', response_model=schemas.Group)
def create_groups(*,
    db: Session = Depends(get_db),
    group_in: schemas.GroupCreate,) -> Any:
    """
        Retrieve Groups.
        """
    return crud_group.create(db=db, obj_in=group_in)
