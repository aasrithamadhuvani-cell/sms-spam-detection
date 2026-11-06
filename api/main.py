import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from api.model_loader import ModelLoader
from api.schemas import SMSRequest, PredictionResponse
from api.monitoring_logger import log_event
loader=ModelLoader()
@asynccontextmanager
async def lifespan(app: FastAPI):
    loader.load()
    yield
app=FastAPI(title="SMS Spam Detection API",version="1.0.0",lifespan=lifespan)
@app.get("/")
def root(): return {"message":"SMS Spam Detection API is running","status":"success"}
@app.get("/health")
def health(): return {"status":"healthy","model_loaded":loader.ready()}
@app.get("/metadata")
def metadata(): return {"service":"SMS Spam Detection API","model_loaded":loader.ready(),"model_uri":loader.model_uri}
@app.post("/predict",response_model=PredictionResponse)
def predict(data: SMSRequest):
    start=time.perf_counter()
    if not loader.ready(): raise HTTPException(status_code=503,detail="Model is not loaded. Train/register a model first.")
    try:
        p=float(loader.model.predict_proba([data.message])[0][1])
        label="spam" if p>=0.5 else "ham"
        log_event({"message_length":len(data.message),"prediction":label,"spam_probability":p,
                   "latency_ms":round((time.perf_counter()-start)*1000,3),"status":"success"})
        return {"prediction":label,"spam_probability":p}
    except Exception as exc:
        log_event({"message_length":len(data.message),"status":"failure","error":str(exc)})
        raise HTTPException(status_code=500,detail="Prediction failed.")
