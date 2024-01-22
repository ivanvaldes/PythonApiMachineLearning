from pydantic import BaseModel

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    language: str