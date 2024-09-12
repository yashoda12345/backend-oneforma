from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class IntrestMapperRepository:
    def create_intrest(self, db: Session, intrest: int, current_user: models.User):
        obj_in_data = {"intrest": intrest, "user_id": current_user.id}
        db_intrest = models.IntrestMapper(**obj_in_data)
        db.add(db_intrest)
        db.commit()
        db.refresh(db_intrest)
        return db_intrest


intrest_mapper = IntrestMapperRepository()
