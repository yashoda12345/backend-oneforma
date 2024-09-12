from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create", response_model=schemas.IndustryResponse)
async def create_industry(*, db: Session = Depends(dependency.get_db),
                          current_user: models.User = Depends(dependency.get_current_user),
                          industry_in: schemas.IndustryCreateBase):
    industry = repository.industry.create_industry(db, industry_in, current_user)
    return industry


@router.get("/all", response_model=List[schemas.IndustryResponse])
async def get_industries(db: Session = Depends(dependency.get_db)):
    industries = repository.industry.get_all_industries(db)
    return industries
