from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base, AuditMixin


class NativeLanguageMapper(Base, AuditMixin):
    __tablename__ = "native_language_mappers"

    native_language = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    is_active = Column(Boolean, default=True)
