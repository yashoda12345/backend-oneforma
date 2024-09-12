from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create")
def create_experience(*, db: Session = Depends(dependency.get_db),
                      current_user: models.User = Depends(dependency.get_current_user),
                      experience_in: List[schemas.ExperienceCreateBase]):
    created_experiences = []
    for experience in experience_in:
        created_experience = repository.experience.create_experience(db, experience,
                                                                     current_user)
        created_experiences.append(created_experience)
    return created_experiences
