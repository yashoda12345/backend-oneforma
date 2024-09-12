from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.get("/all", response_model=List[schemas.UserBase])
async def root(db: Session = Depends(dependency.get_db),
               # current_user: models.User = Depends(dependency.get_current_user)
               ):
    users = db.query(models.User).all()
    # for user in users:
    #     print(user.role_relation.created_at)
    return users


@router.get("/test", response_model=List[schemas.UserBase])
async def get_test(db: Session = Depends(dependency.get_db)):
    users = db.query(models.User).all()
    # for user in users:
    #     print(user.role_relation.created_at)
    return users


@router.post("/create", response_model=schemas.UserInDBBase)
def create_user(
        *,
        db: Session = Depends(dependency.get_db),
        user_in: schemas.UserCreate,
) -> Any:
    """
    Create new user.
    """
    user = repository.user.get_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this Username already exists in the system.",
        )
    user = repository.user.create_user(db, obj_in=user_in)
    return user


@router.post("/update", response_model=schemas.UserInDBBase)
def update_user(
        *,
        db: Session = Depends(dependency.get_db),
        user_in: schemas.UserUpdate,
        current_user: models.User = Depends(dependency.get_current_user),
) -> Any:
    """
    Create new user.
    """
    user = repository.user.get_by_username(db, username=current_user.username)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="The user with this Username doesn't exists in the system.",
        )
    user = repository.user.update_user(db, db_user=user, update_data=user_in)
    return user
