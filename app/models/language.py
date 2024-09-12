from sqlalchemy import Column, String, Boolean

from app.db.base_class import Base, AuditMixin


class Language(Base, AuditMixin):
    __tablename__ = "languages"

    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
