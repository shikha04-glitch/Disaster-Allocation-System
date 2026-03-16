from fastapi import FastAPI
from app.routers import disaster, resource, allocation

app = FastAPI()

app.include_router(disaster.router)
app.include_router(resource.router)
app.include_router(allocation.router)

@app.get("/")
def home():
    return {"message": "Disaster Allocation System Running"}