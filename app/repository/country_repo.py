from sqlalchemy.orm import Session
from app import models
from fastapi.encoders import jsonable_encoder


class CountryRepository:
    def create_country(self, db: Session, country, current_user: models.User):
        obj_in_data = jsonable_encoder(country)
        db_country = models.Country(**obj_in_data)
        db.add(db_country)
        db.commit()
        db.refresh(db_country)
        return db_country

    def get_countries(self, db: Session):
        return db.query(models.Country).all()


country = CountryRepository()
