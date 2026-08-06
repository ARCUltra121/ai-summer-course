def o2_status(level:list):
    crit_count = 0
    low_count = 0
    high_count = 0
    norm_count = 0
    for reading in level:
        print(f'Hour {level.index(reading)}:   {reading}%  -  ', end='')
        if reading > 23:
            high_count += 1
            print('HIGH')
        elif reading <=23 and reading >=19:
            norm_count += 1
            print('NORMAL')
        elif reading <=18 and reading >= 15:
            low_count += 1
            print("LOW")
        elif reading <=15 and reading >=0:
            crit_count += 1
            print('CRITICAL')
            print('*** ALERT: TAKE ACTION IMMEDIATELY ***')
        else:
            print('System Error: Please Take action.')

    print('=== STATUS SUMMARY ===')
    print(f'NORMAL Count: {norm_count}')
    print(f'LOW Count: {low_count}')
    print(f'CRITICAL COUNT: {crit_count}')
    print(f'HIGH Count: {high_count}')


readings = [21, 20, 19, 17, 16, 14, 13, 15, 18, 21, 22, 21]

o2_status(readings)