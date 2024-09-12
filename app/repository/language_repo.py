from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class LanguageRepository:
    def create_language(self, db: Session, language, current_user: models.User):
        obj_in_data = jsonable_encoder(language)
        db_language = models.Language(**obj_in_data)
        db.add(db_language)
        db.commit()
        db.refresh(db_language)
        return db_language

    def get_all_languagess(self, db: Session):
        return db.query(models.Language).all()


language = LanguageRepository()
