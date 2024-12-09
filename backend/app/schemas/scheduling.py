
from pydantic import BaseModel
from typing import List

class SchedulingRequest(BaseModel):
    forecasted_calls: List[float]
    num_agents: int

class SchedulingResponse(BaseModel):
    schedule: List[int]