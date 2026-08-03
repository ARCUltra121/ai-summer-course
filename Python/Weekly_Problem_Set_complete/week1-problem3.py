import time 

soldier_first_name = input("What is the soldier's first name? ")
soldier_last_name =  input("What is the soldier's last name? ")
soldier_rank = input("What is the soldier's rank? ")
push_ups = input("How many push ups were completed? ")
run_time = input("What was the soldier's run time? Format(MM:SS) ").split(":")
run_time_minutes = int(run_time[0])
run_time_seconds = int(run_time[1])
average_pace = ((run_time_minutes * 60) + run_time_seconds) / 2
pace_min = int(average_pace  // 60)
pace_sec = int(average_pace % 60)

def AFT_AAR(first_name, last_name, rank, push_ups, run_time_minutes, run_time_seconds, average_pace, pace_min, pace_sec):
    print(f"=== AFTER-ACTION REPORT ===")
    print(f"Soldier:{rank} {first_name} {last_name}")
    print(f"Push-ups: {push_ups}")
    print(f"2-mile run: {run_time_minutes}:{run_time_seconds}")
    print(f"Average pace: {average_pace} seconds per mile or {pace_min}:{pace_sec} minutes per mile")
    print("DISMISSED")

AFT_AAR(soldier_first_name, soldier_last_name, soldier_rank, push_ups, run_time_minutes, run_time_seconds, average_pace,pace_min, pace_sec)