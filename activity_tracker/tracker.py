# TRACKING MODULE
# Handles time tracking logic

import time
from storage import save_entry


current_activity = None
start_time = None

def start_activity(name):
    # starts tracking time for an activity 
    global current_activity, start_time
    
    if current_activity is not None:
        return "Already tracking an activity!"

    current_activity = name
    start_time = time.time()

    return f"Started: {name}"


def stop_activity():
     # stops tracking and calculates duration
    global current_activity, start_time

    if current_activity is None:
        return "No active session!"

    end_time = time.time()
    duration = end_time - start_time

    minutes = round(duration / 60, 2)

    entry = f"{current_activity} - {minutes} minutes"
    save_entry(entry)

    result = f"Stopped: {current_activity} | Time: {minutes} min"

    current_activity = None
    start_time = None

    return result