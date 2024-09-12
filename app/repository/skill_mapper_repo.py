from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class skillMapperRepository:
    def create_skill(self, db: Session, skill: int, current_user: models.User):
        obj_in_data = {"skill": skill, "user_id": current_user.id}
        db_skill = models.SkillMapper(**obj_in_data)
        db.add(db_skill)
        db.commit()
        db.refresh(db_skill)
        return db_skill


skill_mapper = skillMapperRepository()
