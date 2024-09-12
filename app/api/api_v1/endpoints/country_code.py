from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create", response_model=schemas.CountryCodeResponse)
async def create_country_code(*, db: Session = Depends(dependency.get_db),
                              current_user: models.User = Depends(dependency.get_current_user),
                              country_code_in: schemas.CountryCodeCreateBase):
    country_code = repository.country_code.create_country_code(db, country_code_in, current_user)
    return country_code


@router.get("/all", response_model=List[schemas.CountryCodeResponse])
async def get_country_codes(db: Session = Depends(dependency.get_db)):
    country_codes = repository.country_code.get_country_codes(db)
    return country_codes
