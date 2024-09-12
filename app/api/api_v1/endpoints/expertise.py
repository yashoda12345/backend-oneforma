from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create", response_model=schemas.ExpertiseResponse)
async def create_expertise(*, db: Session = Depends(dependency.get_db),
                           current_user: models.User = Depends(dependency.get_current_user),
                           expertise_in: schemas.ExpertiseCreateBase):
    expertise = repository.expertise.create_expertise(db, expertise_in, current_user)
    return expertise


@router.get("/all", response_model=List[schemas.ExpertiseResponse])
async def get_expertises(db: Session = Depends(dependency.get_db)):
    countries = repository.expertise.get_all_expertise(db)
    return countries
