from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create", response_model=schemas.DegreeResponse)
async def create_degree(*, db: Session = Depends(dependency.get_db),
                        current_user: models.User = Depends(dependency.get_current_user),
                        degree_in: schemas.DegreeCreateBase):
    degree = repository.degree.create_degree(db, degree_in, current_user)
    return degree


@router.get("/all", response_model=List[schemas.DegreeResponse])
async def get_degrees(db: Session = Depends(dependency.get_db)):
    degrees = repository.degree.get_all_degrees(db)
    return degrees
