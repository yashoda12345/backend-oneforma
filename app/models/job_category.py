from sqlalchemy import Column, String, Boolean

from app.db.base_class import Base, AuditMixin


class JobCategory(Base, AuditMixin):
    __tablename__ = "job_categories"

    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
