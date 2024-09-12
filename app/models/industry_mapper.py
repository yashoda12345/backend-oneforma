from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base, AuditMixin


class IndustryMapper(Base, AuditMixin):
    __tablename__ = 'industry_mappers'

    user_id = Column(Integer, ForeignKey("users.id"))
    industry = Column(Integer, ForeignKey("industries.id"))
    industry_relation = relationship("Industry")
    is_active = Column(Boolean, default=True)
