from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create")
def create_industry(*, db: Session = Depends(dependency.get_db),
                    current_user: models.User = Depends(dependency.get_current_user),
                    industry_in: schemas.IndustryMapperCreate):
    created_industries = []
    for industry in industry_in.industry:
        created_industry = repository.industry_mapper.create_industry(db, industry, current_user)
        created_industries.append(created_industry)
    return created_industries
