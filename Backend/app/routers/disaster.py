from fastapi import APIRouter
from app.database import disaster_collection
from app.schemas.disaster import Disaster

router = APIRouter()

@router.post("/disasters")
def create_disaster(disaster: Disaster):

    disaster_collection.insert_one(disaster.dict())

    return {"message": "Disaster added"}