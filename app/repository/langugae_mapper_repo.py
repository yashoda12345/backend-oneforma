from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class LanguageMapperRepository:
    def create_language(self, db: Session, language: int, proficiency: int, current_user: models.User):
        obj_in_data = {"spoken_language": language, "proficiency": proficiency, "user_id": current_user.id}
        db_language = models.LanguageMapper(**obj_in_data)
        db.add(db_language)
        db.commit()
        db.refresh(db_language)
        return db_language


language_mapper = LanguageMapperRepository()
