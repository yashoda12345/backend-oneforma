from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class EthnicityRepository:
    def create_ethnicity(self, db: Session, ethnicity, current_user: models.User):
        obj_in_data = jsonable_encoder(ethnicity)
        db_ethnicity = models.Ethnicity(**obj_in_data)
        db.add(db_ethnicity)
        db.commit()
        db.refresh(db_ethnicity)
        return db_ethnicity

    def get_ethnicities(self, db: Session):
        return db.query(models.Ethnicity).all()


ethnicity = EthnicityRepository()
