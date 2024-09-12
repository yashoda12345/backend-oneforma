from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import as_declarative, declared_attr, declarative_base
import datetime


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, index=True)


class AuditMixin(object):
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
