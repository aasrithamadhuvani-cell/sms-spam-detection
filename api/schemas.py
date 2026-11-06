from pydantic import BaseModel, Field
class SMSRequest(BaseModel):
    message: str = Field(min_length=1, max_length=5000)
class PredictionResponse(BaseModel):
    prediction: str
    spam_probability: float
