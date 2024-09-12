from sqlalchemy import Column, String, Boolean, Integer, ForeignKey

from app.db.base_class import Base, AuditMixin


class State(Base, AuditMixin):
    __tablename__ = 'states'

    name = Column(String, nullable=False)
    country_code = Column(Integer, ForeignKey('countries.name'), primary_key=True)
    is_active = Column(Boolean, default=True)
