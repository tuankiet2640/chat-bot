from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Division(Base):
    __tablename__ = "divisions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    departments = relationship("Department", back_populates="division")
    users = relationship("User", back_populates="division")


    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

# TODO: ADD MORE FIELDS