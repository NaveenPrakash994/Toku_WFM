
from pydantic import BaseModel
from typing import List

class ForecastRequest(BaseModel):
    start_week: int
    end_week: int

class ForecastResponse(BaseModel):
    predictions: List[float]