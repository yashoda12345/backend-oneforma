from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base, AuditMixin, AuditMixin


class EducationMapper(Base, AuditMixin):
    __tablename__ = 'education_mappers'

    user_id = Column(Integer, ForeignKey("users.id"))
    degree = Column(Integer, ForeignKey("degrees.id"))
    field_of_study = Column(String, nullable=False)
    degree_relation = relationship("Degree")
    is_active = Column(Boolean, default=True)
