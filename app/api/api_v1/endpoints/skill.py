from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create", response_model=schemas.SkillResponse)
async def create_skill(*, db: Session = Depends(dependency.get_db),
                       current_user: models.User = Depends(dependency.get_current_user),
                       skill_in: schemas.SkillCreateBase):
    skill = repository.skill.create_skill(db, skill_in, current_user)
    return skill


@router.get("/all", response_model=List[schemas.SkillResponse])
async def get_skills(db: Session = Depends(dependency.get_db)):
    countries = repository.skill.get_all_skills(db)
    return countries
