from fastapi import FastAPI
from mangum import Mangum
from routers import user, pet, pdoc, phr, pr, pt

# Stage name of API Gateway, defined in main.tf
STAGE_NAME = "stage"

app = FastAPI(title="FidoCred Internal API")

app.include_router(user.router)
app.include_router(pet.router)
app.include_router(pdoc.router)
app.include_router(phr.router)
app.include_router(pr.router)
app.include_router(pt.router)

@app.get("/")
def root():
    return {"message": "FidoCred Internal API Up and Running!!"}


handler = Mangum(app, api_gateway_base_path=STAGE_NAME)
