from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create", response_model=schemas.ProficiencyResponse)
async def create_proficiency(*, db: Session = Depends(dependency.get_db),
                             current_user: models.User = Depends(dependency.get_current_user),
                             proficiency_in: schemas.ProficiencyCreateBase):
    proficiency = repository.proficiency.create_proficiency(db, proficiency_in, current_user)
    return proficiency


@router.get("/all", response_model=List[schemas.ProficiencyResponse])
async def get_proficiencies(db: Session = Depends(dependency.get_db)):
    industries = repository.proficiency.get_all_proficiencies(db)
    return industries
