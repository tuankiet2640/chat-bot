from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    division_id = Column(Integer, ForeignKey("divisions.id"))

    department = relationship("Department", back_populates="users")
    division = relationship("Division", back_populates="users")

