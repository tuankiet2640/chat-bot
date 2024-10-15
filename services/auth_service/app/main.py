from fastapi import FastAPI

app = FastAPI(title="Auth Service")

@app.get("/")
async def root():
    return {"message": "Welcome to the Auth Service"}