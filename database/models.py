from sqlalchemy import Column, Integer, String, LargeBinary, DateTime
from database.database import Base
from datetime import datetime
from database.database import engine

class Dbaudio(Base):
    __tablename__ = "audio"
    id = Column(Integer, primary_key=True, index=True)
    audio = Column(LargeBinary)
    timestamp = Column(DateTime, default=datetime.utcnow)

Dbaudio.metadata.create_all(bind=engine)