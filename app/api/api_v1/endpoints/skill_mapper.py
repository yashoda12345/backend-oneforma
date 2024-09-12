from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create")
def create_skill(*, db: Session = Depends(dependency.get_db),
                 current_user: models.User = Depends(dependency.get_current_user),
                 skill_in: schemas.SkillMapperCreate):
    created_skills = []
    for skill in skill_in.skill:
        created_skill = repository.skill_mapper.create_skill(db, skill, current_user)
        created_skills.append(created_skill)
    return created_skills
