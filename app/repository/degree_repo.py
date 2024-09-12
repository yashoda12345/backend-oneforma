from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class DegreeRepository:
    def create_degree(self, db: Session, degree, current_user: models.User):
        obj_in_data = jsonable_encoder(degree)
        db_degree = models.Degree(**obj_in_data)
        db.add(db_degree)
        db.commit()
        db.refresh(db_degree)
        return db_degree

    def get_all_degrees(self, db: Session):
        return db.query(models.Degree).all()


degree = DegreeRepository()
