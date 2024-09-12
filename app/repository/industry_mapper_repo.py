from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class IndustryMapperRepository:
    def create_industry(self, db: Session, industry: int, current_user: models.User):
        obj_in_data = {"industry": industry, "user_id": current_user.id}
        db_industry = models.IndustryMapper(**obj_in_data)
        db.add(db_industry)
        db.commit()
        db.refresh(db_industry)
        return db_industry


industry_mapper = IndustryMapperRepository()
