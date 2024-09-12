from sqlalchemy import Column, String, Boolean

from app.db.base_class import Base, AuditMixin, AuditMixin


class Proficiency(Base, AuditMixin):
    __tablename__ = "proficiencies"

    level = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
