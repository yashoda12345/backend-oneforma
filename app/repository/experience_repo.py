from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class ExperienceRepository:
    def create_experience(self, db: Session, experience, current_user: models.User):
        obj_in_data = jsonable_encoder(experience)
        db_experience = models.WorkExperience(**obj_in_data, user_id=current_user.id)
        db.add(db_experience)
        db.commit()
        db.refresh(db_experience)
        return db_experience


experience = ExperienceRepository()
