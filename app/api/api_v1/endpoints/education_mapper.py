from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create")
def create_education(*, db: Session = Depends(dependency.get_db),
                     current_user: models.User = Depends(dependency.get_current_user),
                     education_in: List[schemas.EducationMapperCreate]):
    created_industries = []
    for education in education_in:
        created_education = repository.education_mapper.create_education(db, education.degree, education.field_of_study,
                                                                         current_user)
        created_industries.append(created_education)
    return created_industries
