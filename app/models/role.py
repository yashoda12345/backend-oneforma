from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
# from app.db.session import Base
from app.db.base_class import Base, AuditMixin


class Role(Base, AuditMixin):
    __tablename__ = "roles"

    # id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    # created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    # updated_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    # created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    # updated_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    #
    # created_by_user = relationship("User", foreign_keys=[created_by], back_populates="created_roles",
    #                                remote_side="User.id")
    # updated_by_user = relationship("User", foreign_keys=[updated_by], back_populates="updated_roles",
    #                                remote_side="User.id")
