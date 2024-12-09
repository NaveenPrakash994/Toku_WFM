from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.ml.forecast_model import forecast_calls
from app.schemas.forecasting import ForecastRequest, ForecastResponse

router = APIRouter()

@router.post("/", response_model=ForecastResponse)
async def forecast(data: ForecastRequest, db: Session = Depends(get_db)):


   # Forecast call volumes based on historical data.
    predictions = forecast_calls(data.start_week, data.end_week, db)
    return {"predictions": predictions}
