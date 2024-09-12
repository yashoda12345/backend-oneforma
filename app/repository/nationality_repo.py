from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class NationalityRepository:
    def create_nationality(self, db: Session, nationality, current_user: models.User):
        obj_in_data = jsonable_encoder(nationality)
        db_nationality = models.Nationality(**obj_in_data)
        db.add(db_nationality)
        db.commit()
        db.refresh(db_nationality)
        return db_nationality

    def get_nationalities(self, db: Session):
        return db.query(models.Nationality).all()


nationality = NationalityRepository()
