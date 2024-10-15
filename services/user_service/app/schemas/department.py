from typing import List, Optional
from pydantic import BaseModel


class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    division_id:int

class DepartmentUpdate(DepartmentBase):
    division_id: Optional[int] = None

class Department(DepartmentBase):
    id: int
    division_id: int

    class Config:
        orm_mode = True
