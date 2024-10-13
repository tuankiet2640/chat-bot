from pydantic import BaseModel
from typing import Optional

class DivisionBase(BaseModel):
    name: str

class DivisionCreate(DivisionBase):
    department_id: int

class DivisionUpdate(DivisionBase):
    department_id: Optional[int] = None

class Division(DivisionBase):
    id: int
    department_id: int

    class Config:
        orm_mode = True
