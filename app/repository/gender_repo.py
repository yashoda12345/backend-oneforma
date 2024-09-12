from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class GenderRepository:
    def create_gender(self, db: Session, gender, current_user: models.User):
        obj_in_data = jsonable_encoder(gender)
        db_gender = models.Gender(**obj_in_data)
        db.add(db_gender)
        db.commit()
        db.refresh(db_gender)
        return db_gender

    def get_genders(self, db: Session):
        return db.query(models.Gender).all()


gender = GenderRepository()
