from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class IntrestRepository:
    def create_intrest(self, db: Session, intrest, current_user: models.User):
        obj_in_data = jsonable_encoder(intrest)
        db_intrest = models.Intrest(**obj_in_data)
        db.add(db_intrest)
        db.commit()
        db.refresh(db_intrest)
        return db_intrest

    def get_all_intrests(self, db: Session):
        return db.query(models.Intrest).all()


intrest = IntrestRepository()
