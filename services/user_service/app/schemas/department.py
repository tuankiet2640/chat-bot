from typing import List, Optional
from pydantic import BaseModel

from app.models.division import Division
from app.models.user import User


class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    users: Optional[List["User"]] = []  # References users in this department
    divisions: Optional[List["Division"]] = []  # References divisions

    class Config:
        orm_mode = True
