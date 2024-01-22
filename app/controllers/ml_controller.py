from fastapi import APIRouter
from model.model import predict_pipeline
from model.model import __version__ as model_version
from models import PredictionOut as PredictionOut
from models import TextIn as TextIn

router = APIRouter()

@router.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@router.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}