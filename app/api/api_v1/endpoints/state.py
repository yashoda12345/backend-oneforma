from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create", response_model=schemas.StateResponse)
async def create_state(*, db: Session = Depends(dependency.get_db),
                       current_user: models.User = Depends(dependency.get_current_user),
                       state_in: schemas.StateCreateBase):
    state = repository.state.create_state(db, state_in, current_user)
    return state


@router.get("/all", response_model=List[schemas.StateResponse])
async def get_states(db: Session = Depends(dependency.get_db)):
    states = repository.state.get_states(db)
    return states
