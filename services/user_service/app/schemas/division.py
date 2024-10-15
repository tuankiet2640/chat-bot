from pydantic import BaseModel
from typing import List, Optional

from app.schemas.department import Department
from app.schemas.user import User


class DivisionBase(BaseModel):
    name: str

class DivisionCreate(DivisionBase):
    pass

class DivisionUpdate(DivisionBase):
    pass

class Division(DivisionBase):
    id: int
    departments: Optional[List["Department"]] = []

    class Config:
        orm_mode = True
