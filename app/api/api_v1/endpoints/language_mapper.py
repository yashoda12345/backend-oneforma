from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, repository
from app.api import dependency

router = APIRouter()


@router.post("/create")
def create_language(*, db: Session = Depends(dependency.get_db),
                    current_user: models.User = Depends(dependency.get_current_user),
                    native_language_in: List[str],
                    language_in: List[schemas.LanguageMapperCreateBase]):
    created_languages = []
    for native in native_language_in:
        repository.native_language_mapper.create_native_language(db, native, current_user)
    for language in language_in:
        created_language = repository.language_mapper.create_language(db, language.spoken_language,
                                                                      language.proficiency, current_user)
        created_languages.append(created_language)
    return created_languages
