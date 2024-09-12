from sqlalchemy import Column, String, Boolean

from app.db.base_class import Base, AuditMixin, AuditMixin


class Expertise(Base, AuditMixin):
    __tablename__ = 'expertise_skills'

    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
