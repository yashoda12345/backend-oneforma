from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base, AuditMixin, AuditMixin


class Job(Base, AuditMixin):
    __tablename__ = "jobs"

    recommended = Column(Boolean, default=False)
    category = Column(Integer, ForeignKey("job_categories.id"))
    job_title = Column(String, nullable=False)
    job_description = Column(Text, nullable=False)
    pay = Column(Integer, nullable=False)
    posted_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=True)
    category_relation = relationship("JobCategory")
