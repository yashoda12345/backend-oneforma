from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class JobRepository:
    def create_job(self, db: Session, job, current_user: models.User):
        obj_in_data = jsonable_encoder(job)
        db_job = models.Job(**obj_in_data)
        db.add(db_job)
        db.commit()
        db.refresh(db_job)
        return db_job

    def get_jobs(self, db: Session):
        return db.query(models.Job).all()


job = JobRepository()
