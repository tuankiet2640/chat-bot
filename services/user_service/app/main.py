from fastapi import FastAPI
from app.api.routes import users, departments, divisions
from app.db.database import engine
from app.models import user, department, division

user.Base.metadata.create_all(bind=engine)
department.Base.metadata.create_all(bind=engine)
division.Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Service")

app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(departments.router, prefix="/api/v1", tags=["departments"])
app.include_router(divisions.router, prefix="/api/v1", tags=["divisions"])

@app.get("/")
async def root():
    return {"message": "Welcome to the User Service",
            "next step": "add /docs to the url"
            }