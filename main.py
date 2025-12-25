from fastapi import FastAPI
from app.routers import auth, tasks

app = FastAPI(title="TaskFlow API")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "Welcome to TaskFlow API"}
