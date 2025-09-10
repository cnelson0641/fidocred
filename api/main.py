from fastapi import FastAPI
from routers import user, pet, pdoc, phr

app = FastAPI(title="FidoCred Internal API")

app.include_router(user.router)
app.include_router(pet.router)
app.include_router(pdoc.router)
app.include_router(phr.router)

@app.get("/")
def root():
    return {"message": "FidoCred Internal API Up and Running!!"}
