import React from "react";
import ForecastChart from "./components/ForecastChart";
import ScheduleTable from "./components/ScheduleTable";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Workforce Management Dashboard</h1>
      <ForecastChart />
      <ScheduleTable />
    </div>
  );
}

export default App;
