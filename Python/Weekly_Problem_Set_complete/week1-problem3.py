import time 

soldier_first_name = input("What is your first name? ")
soldier_last_name =  input("What is your last name? ")
push_ups = input("How many push ups were completed? ")
run_time = input("What was the soldier's run time? ").split(":")
run_time_minutes = int(run_time[0])
run_time_seconds = int(run_time[1])


def AFT_AAR():
    print(f"=== AFTER-ACTION REPORT ===")
    print(f"Soldier:")
    print(f"Push-ups: {push_ups}")
    print(f"2-mile run: {float(run_time)} minutes")
    print(f"Average pace: {float(run_time / 2.0 )} minutes per mile")
    print("DISMISSED")


print(run_time_minutes)
print(run_time_seconds)

