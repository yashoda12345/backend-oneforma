from sqlalchemy import Column, String, Boolean

from app.db.base_class import Base, AuditMixin


class Nationality(Base, AuditMixin):
    __tablename__ = 'nationalities'

    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
