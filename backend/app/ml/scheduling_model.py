import numpy as np

def generate_schedule(forecasted_calls, num_agents):

    #Generate workforce schedules based on forecasted call volumes.
    
    total_calls = sum(forecasted_calls)
    calls_per_agent = total_calls / num_agents

    schedule = []
    for call_volume in forecasted_calls:
        agents_needed = max(1, int(np.ceil(call_volume / calls_per_agent)))
        schedule.append(agents_needed)

    return schedule
