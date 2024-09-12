from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base, AuditMixin


class SkillMapper(Base, AuditMixin):
    __tablename__ = 'skill_mappers'

    user_id = Column(Integer, ForeignKey("users.id"))
    skill = Column(Integer, ForeignKey("skills.id"))
    skill_relation = relationship("Skill")
    is_active = Column(Boolean, default=True)
