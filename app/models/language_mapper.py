from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base, AuditMixin


class LanguageMapper(Base, AuditMixin):
    __tablename__ = "language_mappers"

    spoken_language = Column(Integer, ForeignKey("languages.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    proficiency = Column(Integer, ForeignKey("proficiencies.id"), nullable=False)
    is_active = Column(Boolean, default=True)
