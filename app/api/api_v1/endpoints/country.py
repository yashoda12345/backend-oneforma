from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create", response_model=schemas.CountryResponse)
async def create_country(*, db: Session = Depends(dependency.get_db),
                         current_user: models.User = Depends(dependency.get_current_user),
                         country_in: schemas.CountryCreateBase):
    country = repository.country.create_country(db, country_in, current_user)
    return country


@router.get("/all", response_model=List[schemas.CountryResponse])
async def get_countries(db: Session = Depends(dependency.get_db)):
    countries = repository.country.get_countries(db)
    return countries
