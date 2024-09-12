from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class ProficiencyRepository:
    def create_proficiency(self, db: Session, proficiency, current_user: models.User):
        obj_in_data = jsonable_encoder(proficiency)
        db_proficiency = models.Proficiency(**obj_in_data)
        db.add(db_proficiency)
        db.commit()
        db.refresh(db_proficiency)
        return db_proficiency

    def get_all_proficiencies(self, db: Session):
        return db.query(models.Proficiency).all()


proficiency = ProficiencyRepository()
