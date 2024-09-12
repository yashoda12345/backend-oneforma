from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.get("/all", response_model=List[schemas.JobListResponse])
async def get_jobs(db: Session = Depends(dependency.get_db)):
    jobs = repository.job.get_jobs(db)
    return jobs


@router.post("/create", response_model=schemas.JobBase)
async def create_job(*, db: Session = Depends(dependency.get_db),
                     current_user: models.User = Depends(dependency.get_current_user), job_in: schemas.JobBase):
    job = repository.job.create_job(db, job_in, current_user)
    return job
