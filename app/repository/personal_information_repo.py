from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class PersonalInformationRepository:
    def create_job(self, db: Session, information, current_user: models.User):
        obj_in_data = jsonable_encoder(information)
        db_information = models.PersonalInformation(**obj_in_data, user_id=current_user.id)
        db.add(db_information)
        db.commit()
        db.refresh(db_information)
        return db_information

    def get_jobs(self, db: Session):
        return db.query(models.PersonalInformation).all()


personal_information = PersonalInformationRepository()
