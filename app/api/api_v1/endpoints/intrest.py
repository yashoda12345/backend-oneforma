from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create", response_model=schemas.IntrestResponse)
async def create_intrest(*, db: Session = Depends(dependency.get_db),
                         current_user: models.User = Depends(dependency.get_current_user),
                         intrest_in: schemas.IntrestCreateBase):
    intrest = repository.intrest.create_intrest(db, intrest_in, current_user)
    return intrest


@router.get("/all", response_model=List[schemas.IntrestResponse])
async def get_intrests(db: Session = Depends(dependency.get_db)):
    countries = repository.intrest.get_all_intrests(db)
    return countries
