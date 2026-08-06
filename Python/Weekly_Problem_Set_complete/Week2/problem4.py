def check_fitness(score):
    if score >= 70:
        return True
    else:
        return False

def check_rank(rank):
    ranks = ['Corporal', 'Sergeant', 'Lieutenant']
    checker = False
    for i in ranks:
        if rank == ranks[i]:
            checker = True
        else:
            pass
    return checker
def check_service_years(years):
    if years >=2:
        return True
    else:
        return False