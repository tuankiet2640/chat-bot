from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    name: str
    email: EmailStr
    password: str
    is_active: bool = True
    department_id: int = None
    division_id: int = None


class UserUpdate(UserBase):
    password: str | None = None

class User(UserBase):
    id: int
    class Config:
        orm_mode = True 