from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class ExpertiseMapperRepository:
    def create_expertise(self, db: Session, expertise: int, current_user: models.User):
        obj_in_data = {"expertise": expertise, "user_id": current_user.id}
        db_expertise = models.ExpertiseMapper(**obj_in_data)
        db.add(db_expertise)
        db.commit()
        db.refresh(db_expertise)
        return db_expertise


expertise_mapper = ExpertiseMapperRepository()
