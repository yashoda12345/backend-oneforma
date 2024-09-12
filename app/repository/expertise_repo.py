from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class ExpertiseRepository:
    def create_expertise(self, db: Session, expertise, current_user: models.User):
        obj_in_data = jsonable_encoder(expertise)
        db_expertise = models.Expertise(**obj_in_data)
        db.add(db_expertise)
        db.commit()
        db.refresh(db_expertise)
        return db_expertise

    def get_all_expertise(self, db: Session):
        return db.query(models.Expertise).all()


expertise = ExpertiseRepository()
