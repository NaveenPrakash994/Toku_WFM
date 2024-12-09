import React, { useState } from "react";
import axios from "../api/axios";

const ScheduleTable = () => {
  const [schedule, setSchedule] = useState([]);
  const [numAgents, setNumAgents] = useState(10);

  const fetchSchedule = async () => {
    try {
      const response = await axios.post("/schedule/", {
        forecasted_calls: [100, 200, 150, 180, 130],
        num_agents: numAgents,
      });
      setSchedule(response.data.schedule);
    } catch (error) {
      console.error("Error generating schedule:", error);
    }
  };

  return (
    <div>
      <h2>Agent Scheduling</h2>
      <input
        type="number"
        value={numAgents}
        onChange={(e) => setNumAgents(e.target.value)}
        placeholder="Enter number of agents"
      />
      <button onClick={fetchSchedule}>Generate Schedule</button>
      <table>
        <thead>
          <tr>
            <th>Time Slot</th>
            <th>Agents Assigned</th>
          </tr>
        </thead>
        <tbody>
          {schedule.map((agents, index) => (
            <tr key={index}>
              <td>Slot {index + 1}</td>
              <td>{agents}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ScheduleTable;
