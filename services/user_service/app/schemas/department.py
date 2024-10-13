from typing import List, Optional
from pydantic import BaseModel

from app.schemas.division import Division
from app.schemas.user import User


class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    users: Optional[List["User"]] = []
    divisions: Optional[List["Division"]] = []

    class Config:
        orm_mode = True
