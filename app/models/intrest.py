from sqlalchemy import Column, String, Boolean

from app.db.base_class import Base, AuditMixin


class Intrest(Base, AuditMixin):
    __tablename__ = 'intrests'

    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
