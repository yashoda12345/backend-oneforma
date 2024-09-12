from sqlalchemy import Column, String, Boolean

from app.db.base_class import Base, AuditMixin, AuditMixin


class Country(Base, AuditMixin):
    __tablename__ = 'countries'

    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
