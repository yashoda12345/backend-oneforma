from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class NativeLanguageMapperRepository:
    def create_native_language(self, db: Session, native_language: str, current_user: models.User):
        obj_in_data = {"native_language": native_language, "user_id": current_user.id}
        db_native_language = models.NativeLanguageMapper(**obj_in_data)
        db.add(db_native_language)
        db.commit()
        db.refresh(db_native_language)
        return db_native_language


native_language_mapper = NativeLanguageMapperRepository()
