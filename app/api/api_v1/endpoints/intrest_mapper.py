from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create")
def create_intrest(*, db: Session = Depends(dependency.get_db),
                   current_user: models.User = Depends(dependency.get_current_user),
                   intrest_in: schemas.IntrestMapperCreate):
    created_intrests = []
    for intrest in intrest_in.intrest:
        created_intrest = repository.intrest_mapper.create_intrest(db, intrest, current_user)
        created_intrests.append(created_intrest)
    return created_intrests
