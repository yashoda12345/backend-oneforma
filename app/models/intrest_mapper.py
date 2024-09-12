from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base, AuditMixin


class IntrestMapper(Base, AuditMixin):
    __tablename__ = 'intrest_mappers'

    user_id = Column(Integer, ForeignKey("users.id"))
    intrest = Column(Integer, ForeignKey("intrests.id"))
    intrest_relation = relationship("Intrest")
    is_active = Column(Boolean, default=True)
