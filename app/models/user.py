from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
# from app.db.session import Base
from app.models.role import Role
from app.db.base_class import Base, AuditMixin


class User(Base, AuditMixin):
    __tablename__ = "users"

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    otp = Column(Integer, nullable=True)
    logged_in = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    role = Column(Integer, ForeignKey("roles.id"), nullable=True)
    linkedin_url = Column(String, nullable=True)
    agreed_nda = Column(Boolean, default=False)
    role_relation = relationship("Role", foreign_keys=[role])
