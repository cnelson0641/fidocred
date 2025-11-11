from fastapi import FastAPI, HTTPException
from mangum import Mangum
#from api.routers import user, pet, pdoc, phr, pr, pt
from api.routers import user
from db.db import engine
from sqlmodel import SQLModel

app = FastAPI(title="FidoCred Internal API")

app.include_router(user.router)
#app.include_router(pet.router)
#app.include_router(pdoc.router)
#app.include_router(phr.router)
#app.include_router(pr.router)
#app.include_router(pt.router)

# Base Hello World
@app.get("/")
def root():
    return {"message": "FidoCred Internal API Up and Running!!"}

# Path not found
@app.get("/{full_path:path}")
def catch_all(full_path: str):
    raise HTTPException(status_code=404, detail=f"Endpoint /{full_path} not found")

# Startup hook: create tables if they don't exist
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    print("Tables ensured in DB!")

# For AWS Lambda, does not affect local execution
handler = Mangum(app)
