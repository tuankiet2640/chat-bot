from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, declarative_base, Mapped, mapped_column
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)  # Corrected here
    department_id = Column(Integer, ForeignKey("departments.id"))
    division_id = Column(Integer, ForeignKey("divisions.id"))
    department = relationship("Department", back_populates="users")
    division = relationship("Division", back_populates="users")
    class Config:

        from_attributes = True
        arbitrary_types_allowed = True
