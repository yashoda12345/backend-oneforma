from sqlalchemy import Column, String, Boolean

from app.db.base_class import Base, AuditMixin


class Skill(Base, AuditMixin):
    __tablename__ = 'skills'

    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
