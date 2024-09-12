from sqlalchemy import Column, String, Boolean

from app.db.base_class import Base, AuditMixin, AuditMixin


class Degree(Base, AuditMixin):
    __tablename__ = 'degrees'

    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
