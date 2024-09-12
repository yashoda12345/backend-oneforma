from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class IndustryRepository:
    def create_industry(self, db: Session, industry, current_user: models.User):
        obj_in_data = jsonable_encoder(industry)
        db_industry = models.Industry(**obj_in_data)
        db.add(db_industry)
        db.commit()
        db.refresh(db_industry)
        return db_industry

    def get_all_industries(self, db: Session):
        return db.query(models.Industry).all()


industry = IndustryRepository()
