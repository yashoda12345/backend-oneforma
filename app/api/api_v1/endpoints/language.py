from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create", response_model=schemas.LanguageResponse)
async def create_language(*, db: Session = Depends(dependency.get_db),
                          current_user: models.User = Depends(dependency.get_current_user),
                          language_in: schemas.LanguageCreateBase):
    language = repository.language.create_language(db, language_in, current_user)
    return language


@router.get("/all", response_model=List[schemas.LanguageResponse])
async def get_languages(db: Session = Depends(dependency.get_db)):
    industries = repository.language.get_all_languagess(db)
    return industries
