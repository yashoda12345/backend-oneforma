from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create", response_model=schemas.GenderResponse)
async def create_gender(*, db: Session = Depends(dependency.get_db),
                        current_user: models.User = Depends(dependency.get_current_user),
                        gender_in: schemas.GenderCreateBase):
    gender = repository.gender.create_gender(db, gender_in, current_user)
    return gender


@router.get("/all", response_model=List[schemas.GenderResponse])
async def get_genders(db: Session = Depends(dependency.get_db)):
    genders = repository.gender.get_genders(db)
    return genders
