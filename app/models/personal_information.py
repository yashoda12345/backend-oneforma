from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base, AuditMixin


class PersonalInformation(Base, AuditMixin):
    __tablename__ = 'personal_informations'

    user_id = Column(Integer, ForeignKey('users.id'))
    gender = Column(Integer, ForeignKey('genders.id'))
    nationality = Column(Integer, ForeignKey('nationalities.id'))
    ethnicity = Column(Integer, ForeignKey('ethnicities.id'))
    street_address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(Integer, ForeignKey('states.id'))
    country_code = Column(Integer, ForeignKey('country_codes.code'))
    postal_code = Column(Integer, nullable=False)
    mobile = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    optional_number = Column(String)
    is_active = Column(Boolean, default=True)

    gender_id = relationship("Gender")
    nationality_relation = relationship("Nationality")
    ethnicity_relation = relationship("Ethnicity")
    state_relation = relationship("State")
    country_code_relation = relationship("CountryCode")
