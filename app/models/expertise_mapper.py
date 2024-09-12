from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base, AuditMixin


class ExpertiseMapper(Base, AuditMixin):
    __tablename__ = 'expertise_mappers'

    user_id = Column(Integer, ForeignKey("users.id"))
    expertise = Column(Integer, ForeignKey("expertise_skills.id"))
    expertise_relation = relationship("Expertise")
    is_active = Column(Boolean, default=True)
