from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class StateRepository:
    def create_state(self, db: Session, state, current_user: models.User):
        obj_in_data = jsonable_encoder(state)
        db_state = models.State(**obj_in_data)
        db.add(db_state)
        db.commit()
        db.refresh(db_state)
        return db_state

    def get_states(self, db: Session):
        return db.query(models.State).all()


state = StateRepository()
