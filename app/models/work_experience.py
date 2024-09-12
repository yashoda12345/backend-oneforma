from sqlalchemy import Column, String, Boolean, Date, Integer, ForeignKey

from app.db.base_class import Base, AuditMixin


class WorkExperience(Base, AuditMixin):
    __tablename__ = 'experiences'

    user_id = Column(Integer, ForeignKey("users.id"))
    role = Column(String, nullable=False)
    company = Column(String, nullable=False)
    start_year = Column(Date, nullable=False)
    end_year = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
