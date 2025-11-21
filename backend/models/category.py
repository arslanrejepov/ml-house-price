from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import func
from backend.database import Base

def Category(Base):
    __tablename__="categories"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    