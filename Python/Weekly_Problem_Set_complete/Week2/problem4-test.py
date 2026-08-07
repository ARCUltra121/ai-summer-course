import problem4

name = input('What is your name soldier? ')
fitness_score = int(input('What is your current fitness score? '))
rank = input('What is your rank soldier? ')
years = int(input('How many years of service do you have? '))

def clearance_report(name, score, rank, years):
    fitness_check = problem4.check_fitness(score)
    rank_check = problem4.check_rank(rank)
    service_check = problem4.check_service_years(years)
    print(f'SOLDIER NAME: {name}')
    print(f'FITNESS SCORE: {score}')
    print(f'RANK: {rank}')
    print(f'YEARS OF SERVICE: {years}')
    print(f'')
    print(f'=== MISSION CLEARANCE REPORT ===')
    if fitness_check:    
        print(f'FITNESS CHECK: PASS')
    else:
        print(f'FITNESS CHECK: FAIL')

    if rank_check:
        print(f'RANK CHECK: PASS')
    else:
        print(f'RANK CHECK: FAIL')

    if service_check:
        print(f'SERVICE CHECK: PASS')
    else:
        print(f'SERVICE CHECK: FAIL')

    if fitness_check and rank_check and service_check:
        print(f'FINAL STATUS: CLEARED FOR MISSION')
    else:
        print(f'FINAL STATUS: NOT CLEARED FOR MISSION')

clearance_report(name,fitness_score,rank,years)