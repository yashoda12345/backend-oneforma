from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class CountryCodeRepository:
    def create_country_code(self, db: Session, country_code, current_user: models.User):
        obj_in_data = jsonable_encoder(country_code)
        db_country_code = models.CountryCode(**obj_in_data)
        db.add(db_country_code)
        db.commit()
        db.refresh(db_country_code)
        return db_country_code

    def get_country_codes(self, db: Session):
        return db.query(models.CountryCode).all()


country_code = CountryCodeRepository()
