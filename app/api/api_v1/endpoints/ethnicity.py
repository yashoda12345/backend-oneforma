from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create", response_model=schemas.EthnicityResponse)
async def create_ethnicity(*, db: Session = Depends(dependency.get_db),
                           current_user: models.User = Depends(dependency.get_current_user),
                           ethnicity_in: schemas.EthnicityCreateBase):
    ethnicity = repository.ethnicity.create_ethnicity(db, ethnicity_in, current_user)
    return ethnicity


@router.get("/all", response_model=List[schemas.EthnicityResponse])
async def get_ethnicities(db: Session = Depends(dependency.get_db)):
    ethnicities = repository.ethnicity.get_ethnicities(db)
    return ethnicities
