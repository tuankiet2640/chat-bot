from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    division_id = Column(Integer, ForeignKey("divisions.id"))

    users = relationship("User", back_populates="department")
    division = relationship("Division", back_populates="departments")

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

# TODO: ADD MORE FIELDS