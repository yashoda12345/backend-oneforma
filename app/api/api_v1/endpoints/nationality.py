from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create", response_model=schemas.NationalityResponse)
async def create_nationality(*, db: Session = Depends(dependency.get_db),
                             current_user: models.User = Depends(dependency.get_current_user),
                             nationality_in: schemas.NationalityCreateBase):
    nationality = repository.nationality.create_nationality(db, nationality_in, current_user)
    return nationality


@router.get("/all", response_model=List[schemas.NationalityResponse])
async def get_nationalities(db: Session = Depends(dependency.get_db)):
    nationalities = repository.nationality.get_nationalities(db)
    return nationalities
