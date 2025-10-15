import sqlite3
import json

conn = sqlite3.connect("historical_data.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS heartrate_zones")
cur.execute("CREATE TABLE IF NOT EXISTS heartrate_zones (zone_name, min_hr, max_hr)") # heart rate zones that only change by different age
cur.execute("INSERT INTO heartrate_zones VALUES ('Out of Range', 30, 118), ('Fat Burn', 119, 144), ('Cardio', 145, 175), ('Peak', 176, 220)")

cur.execute("DROP TABLE IF EXISTS activities")
cur.execute("CREATE TABLE IF NOT EXISTS activities (" \
"log_ID PRIMARY KEY, activity_name, calories, distance, steps, elevation_gain, speed, pace, avg_heartrate, start_time, duration_ms, active_duration_ms, " \
"hr_outofrange_mins, hr_fatburn_mins, hr_cardio_mins, hr_peak_mins," \
"calories_link, heartrate_link, tcx_link, raw_json)") # save activity log list
cur.execute("CREATE TABLE IF NOT EXISTS active_zone_mins (" \
"azm_id INTEGER PRIMARY KEY AUTOINCREMENT," \
"activity_id, zone_name, mins, min_multiplier," \
"FOREIGN KEY (activity_id) REFERENCES activities (activity_id))")

cur.execute("DROP TABLE IF EXISTS vo2_max")
cur.execute("CREATE TABLE IF NOT EXISTS vo2_max (date PRIMARY KEY, value)") # cardio fitness score

cur.execute("DROP TABLE IF EXISTS heart_rate_intraday")
cur.execute("CREATE TABLE heart_rate_intraday (date, time, value)") # intraday heart rate

# cur.execute("CREATE TABLE oxygen_sat (date, steps)") # oxygen saturation during sleep TODO
# cur.execute("CREATE TABLE resp_rate (date, steps)") # respiratory rate during sleep TODO

cur.execute("DROP TABLE IF EXISTS sleep_logs")
cur.execute("CREATE TABLE IF NOT EXISTS sleep_logs (log_id PRIMARY KEY, date, duration_ms, efficiency, starttime, endtime," \
"infoCode, is_main_sleep," \
"deep_count, deep_minutes, thirty_day_avg_deep_mins," \
"light_count, light_mins, thirty_day_avg_light_mins," \
"rem_count, rem_mins, thirty_day_avg_rem_mins," \
"wake_count, wake_mins, thirty_day_avg_wake_mins," \
"mins_after_wakeup, mins_awake, mins_asleep, mins_to_fall_asleep, time_in_bed)") # sleep data, probably drop sleep level counts and calculate from sleep_details table instead (storage-optimized)
cur.execute("DROP TABLE IF EXISTS sleep_details")
cur.execute("CREATE TABLE IF NOT EXISTS sleep_details (log_id, date, time, sleep_level," \
"FOREIGN KEY (log_id) REFERENCES sleep_logs (log_id))")

cur.execute("DROP TABLE IF EXISTS skin_temp_sleeping")
cur.execute("CREATE TABLE IF NOT EXISTS skin_temp_sleeping (date PRIMARY KEY, nightly_relative)") # skin temperature during sleep

cur.execute("DROP TABLE IF EXISTS weight_logs")
cur.execute("CREATE TABLE weight_logs (date PRIMARY KEY, log_id SECONDARY KEY, weight, bmi)") # weight logs

# with open("./historical_data/sleep.json", "r") as json_file:
#     data = json.load(json_file)
#     for item in data:
#         conn.execute("INSERT INTO steps (date, steps) VALUES (?, ?)", (item["date"], item["steps"]))
conn.commit()
# res = cur.execute("SELECT min_hr FROM heartrate_zones")
# res.fetchall()
conn.close()