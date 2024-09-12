from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create")
async def create_information(*, db: Session = Depends(dependency.get_db),
                             current_user: models.User = Depends(dependency.get_current_user),
                             information_in: schemas.PersonalInformationCreate
                             ):
    personal_information = repository.personal_information.create_job(db, information_in, current_user)
    return personal_information
