from fastapi import APIRouter
from app.api.v1.endpoints.imageGenerate import generate_image


generateImage = APIRouter()

generateImage.post("/get-image")(generate_image)