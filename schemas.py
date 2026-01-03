from pydantic import BaseModel
from typing import Optional

# ---------- User ----------
class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    role: str

    class Config:
        orm_mode = True

# ---------- Task ----------
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]

    class Config:
        orm_mode = True
