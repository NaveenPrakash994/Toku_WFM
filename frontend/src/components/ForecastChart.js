import React, { useState } from "react";
import axios from "../api/axios";
import { Line } from "react-chartjs-2";

const ForecastChart = () => {
  const [predictions, setPredictions] = useState([]);

  const fetchForecast = async () => {
    try {
      const response = await axios.post("/forecast/", { start_week: 1, end_week: 5 });
      setPredictions(response.data.predictions);
    } catch (error) {
      console.error("Error fetching forecast:", error);
    }
  };

  const chartData = {
    labels: Array.from({ length: predictions.length }, (_, i) => `Week ${i + 1}`),
    datasets: [
      {
        label: "Forecasted Call Volume",
        data: predictions,
        borderColor: "rgba(75,192,192,1)",
        borderWidth: 2,
      },
    ],
  };

  return (
    <div>
      <h2>Call Volume Forecast</h2>
      <button onClick={fetchForecast}>Fetch Forecast</button>
      <Line data={chartData} />
    </div>
  );
};

export default ForecastChart;
