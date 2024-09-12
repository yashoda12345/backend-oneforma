from sqlalchemy.orm import Session
from app import models


class EducationMapperRepository:
    def create_education(self, db: Session, degree: int, field_of_study: str, current_user: models.User):
        obj_in_data = {"degree": degree, "field_of_study": field_of_study, "user_id": current_user.id}
        db_education = models.EducationMapper(**obj_in_data)
        db.add(db_education)
        db.commit()
        db.refresh(db_education)
        return db_education


education_mapper = EducationMapperRepository()
