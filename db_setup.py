import sqlite3
import json

conn = sqlite3.connect("historical_data.db")
cur = conn.cursor()

cur.execute("CREATE TABLE heartrate_zones (zone_name, min_hr, max_hr)") # heart rate zones that only change by different age
cur.execute("INSERT INTO heartrate_zones VALUES ('Out of Range', 30, 118), ('Fat Burn', 119, 144), ('Cardio', 145, 175), ('Peak', 176, 220)")
# cur.execute("CREATE TABLE activities (" \
# "log_ID PRIMARY KEY, activity_name, calories, distance, steps, speed, pace, avg_heartrate, duration, active_duration, " \
# "lvl_sedentary_mins, lvl_lightly_mins, lvl_fairly_mins, lvl_very_mins)") # save activity log list
# cur.execute("CREATE TABLE vo2_max (date, steps)") # cardio fitness score
# cur.execute("CREATE TABLE heart_rate (date, steps)") # intraday heart rate
# cur.execute("CREATE TABLE oxygen_sat (date, steps)") # oxygen saturation during sleep
# cur.execute("CREATE TABLE resp_rate (date, steps)") # respiratory rate during sleep
# cur.execute("CREATE TABLE sleep (date, steps)") # sleep data
# cur.execute("CREATE TABLE temperature (date, steps)") # skin temperature during sleep
# cur.execute("CREATE TABLE weight (date, steps)") # weight logs

# with open("./historical_data/sleep.json", "r") as json_file:
#     data = json.load(json_file)
#     for item in data:
#         conn.execute("INSERT INTO steps (date, steps) VALUES (?, ?)", (item["date"], item["steps"]))
conn.commit()
# res = cur.execute("SELECT min_hr FROM heartrate_zones")
# res.fetchall()
conn.close()