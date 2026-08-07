athletes = [
    ("Jordan",  82, 15),   # (name, games_played, goals_scored)
    ("Patel",   78, 22),
    ("Okonkwo", 90, 18),
    ("Li",      65, 9),
    ("Reyes",   88, 31),
    ("Fischer", 72, 14),
]
athlete_modified ={}
top_scorer = None
top_goals = 0

def goals_per_game():
    for athlete in athletes:
        gpg = athlete[2] / athlete[1]
        athlete_modified[athlete[0]] = {}
        athlete_modified[athlete[0]]['games'] = athlete[1]
        athlete_modified[athlete[0]]['goals'] = athlete[2]
        athlete_modified[athlete[0]]['gpg'] = round(gpg, 2)
        athlete_modified[athlete[0]]['Candidate'] = mvp_candidate(gpg)

def mvp_candidate(gpg):
    if gpg >= 0.25:
        return True
    else:
        return False

goals_per_game()

print(athlete_modified)



print(f'=== SEASON LEADERBOARD ===')
print(f'ATHLETE  GAMES  GOALS  GPG  MVP?')
print(f'________________________________')
for athlete, inner in athlete_modified.items():
    print(f'{athlete}', end="\t")
    for stat, value in inner.items():
        print(f'{value} ', end="\t")
        if stat =='goals':
            if value > top_goals:
                top_scorer = athlete
                top_goals = value
    print()

 
print(f'')


print(f'Top scorer: {top_scorer} ({top_goals} goals)')