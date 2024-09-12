from sqlalchemy import Column, String, Boolean

from app.db.base_class import Base, AuditMixin, AuditMixin


class Industry(Base, AuditMixin):
    __tablename__ = 'industries'

    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
