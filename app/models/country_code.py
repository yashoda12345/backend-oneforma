from sqlalchemy import Column, String, Boolean, Integer, ForeignKey

from app.db.base_class import Base, AuditMixin, AuditMixin


class CountryCode(Base, ):
    __tablename__ = 'country_codes'

    code = Column(Integer, nullable=False)
    country = Column(String, ForeignKey('countries.name'), nullable=False)
    is_active = Column(Boolean, default=True)
