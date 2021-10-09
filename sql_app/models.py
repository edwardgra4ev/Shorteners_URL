from sqlalchemy import Column, String, DateTime, Integer
from sql_app.database import Base
import datetime
from uuid import uuid4


def uid() -> str:
    return str(uuid4())


# Таблица URL
class URL(Base):
    __tablename__ = "URL"
    uid = Column(String, default=uid, primary_key=True, index=True)
    url = Column(String, index=True)
    url_shorter = Column(String, unique=True, index=True)
    date_creation = Column(DateTime, default=datetime.datetime.utcnow)
    count_requests = Column(Integer, default=0)
