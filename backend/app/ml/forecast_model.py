import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sqlalchemy.orm import Session
from app.db.models import CallData

def forecast_calls(start_week: int, end_week: int, db: Session):
    """
    Use Exponential Smoothing for time series forecasting.
    """
    # Query historical data from the database
    query = db.query(CallData).all()
    data = pd.DataFrame([{
        "week": row.week,
        "call_volume": row.call_volume
    } for row in query])

    # Ensure the data is sorted
    data = data.sort_values(by="week")
    
    # Fit the time series model
    model = ExponentialSmoothing(data["call_volume"], seasonal="add", seasonal_periods=4)
    fit = model.fit()

    # Forecast for the specified weeks
    future = list(range(start_week, end_week + 1))
    predictions = fit.forecast(len(future)).tolist()

    return predictions
