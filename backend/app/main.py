from fastapi import FastAPI
from app.api.forecasting import router as forecasting_router
from app.api.scheduling import router as scheduling_router

app = FastAPI(title="Workforce Management API")

# Include routers
app.include_router(forecasting_router, prefix="/forecast", tags=["Forecasting"])
app.include_router(scheduling_router, prefix="/schedule", tags=["Scheduling"])

@app.get("/")
def root():
    return {"message": "Welcome to the Workforce Management API"}
