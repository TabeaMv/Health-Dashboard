import sqlite3
import json

conn = sqlite3.connect("historical_data.db")

conn.execute("CREATE TABLE heartrate_zones (zone_name, min_hr, max_hr)") # heart rate zones that only change by different age
conn.execute("CREATE TABLE activities (" \
"log_ID PRIMARY KEY, activity_name, calories, distance, steps, speed, pace, avg_heartrate, duration, active_duration, " \
"lvl_sedentary_mins, lvl_lightly_mins, lvl_fairly_mins, lvl_very_mins)") # save activity log list
conn.execute("CREATE TABLE vo2_max (date, steps)") # cardio fitness score
conn.execute("CREATE TABLE heart_rate (date, steps)") # intraday heart rate
conn.execute("CREATE TABLE oxygen_sat (date, steps)") # oxygen saturation during sleep
conn.execute("CREATE TABLE resp_rate (date, steps)") # respiratory rate during sleep
conn.execute("CREATE TABLE sleep (date, steps)") # sleep data
conn.execute("CREATE TABLE temperature (date, steps)") # skin temperature during sleep
conn.execute("CREATE TABLE weight (date, steps)") # weight logs

# with open("./historical_data/sleep.json", "r") as json_file:
#     data = json.load(json_file)
#     for item in data:
#         conn.execute("INSERT INTO steps (date, steps) VALUES (?, ?)", (item["date"], item["steps"]))
conn.commit()
conn.close()