from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create")
def create_expertise(*, db: Session = Depends(dependency.get_db),
                     current_user: models.User = Depends(dependency.get_current_user),
                     expertise_in: schemas.ExpertiseMapperCreate):
    created_expertises = []
    for expertise in expertise_in.expertise:
        created_expertise = repository.expertise_mapper.create_expertise(db, expertise, current_user)
        created_expertises.append(created_expertise)
    return created_expertises
