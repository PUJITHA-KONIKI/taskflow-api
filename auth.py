from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserLogin
from app.models.user import User
from app.auth.jwt_handler import sign_jwt
from app.auth.hashing import Hash

router = APIRouter()

# In-memory users for example (replace with DB)
users_db = []

@router.post("/signup")
def signup(user: UserCreate):
    if any(u["email"] == user.email for u in users_db):
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = Hash.bcrypt(user.password)
    users_db.append({"email": user.email, "password": hashed_password, "role": user.role})
    return {"message": "User created successfully"}

@router.post("/login")
def login(user: UserLogin):
    db_user = next((u for u in users_db if u["email"] == user.email), None)
    if not db_user or not Hash.verify(db_user["password"], user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = sign_jwt(db_user["email"])
    return {"token": token}
