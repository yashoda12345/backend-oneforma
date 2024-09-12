from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class SkillRepository:
    def create_skill(self, db: Session, skill, current_user: models.User):
        obj_in_data = jsonable_encoder(skill)
        db_skill = models.Skill(**obj_in_data)
        db.add(db_skill)
        db.commit()
        db.refresh(db_skill)
        return db_skill

    def get_all_skills(self, db: Session):
        return db.query(models.Skill).all()


skill = SkillRepository()
