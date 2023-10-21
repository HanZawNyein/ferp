from typing import List, Any, TypeVar
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ferp.db import Base
from ferp.db.dependencies import get_db

from . import schemas
from .crud import group as crud_group

router = APIRouter(tags=["Hello"])

ModelType = TypeVar("ModelType", bound=Base)


@router.get('/', response_model=List[schemas.Group])
def read_groups(db: Session = Depends(get_db),
                skip: int = 0,
                limit: int = 100) -> Any:
    """
    Retrieve Groups.
    """
    return crud_group.get_multi(db=db, skip=skip, limit=limit)


@router.get("/{id}", response_model=schemas.Group)
def read_group(
        *,
        db: Session = Depends(get_db),
        id: int
) -> Any:
    """
    Get group by ID.
    """
    item = crud_group.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Group not found")
    return item


@router.post('/', response_model=schemas.Group)
def create_groups(*,
                  db: Session = Depends(get_db),
                  group_in: schemas.GroupCreate, ) -> Any:
    """
    Create Groups.
    """
    group = crud_group.create(db=db, obj_in=group_in)
    return group


@router.put("/{id}", response_model=schemas.Group)
def update_item(
        *,
        db: Session = Depends(get_db),
        id: int,
        group_in: schemas.GroupUpdate,
) -> Any:
    """
    Update a group.
    """
    item = crud_group.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Group not found")
    item = crud_group.update(db=db, db_obj=item, obj_in=group_in)
    return item


@router.delete("/{id}", response_model=schemas.Group)
def delete_item(
        *,
        db: Session = Depends(get_db),
        id: int,
) -> Any:
    """
    Delete a group.
    """
    item = crud_group.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Group not found")
    item = crud_group.remove(db=db, id=id)
    return item
