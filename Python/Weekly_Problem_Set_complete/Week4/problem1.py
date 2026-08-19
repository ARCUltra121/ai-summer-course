reports = [
    "SANTOS | Private | Fitness:91 | Status:available",
    "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
    "OKAFOR | Sergeant | Fitness:88 | Status:available",
    "BRIGGS | Private | Fitness:55 | Status:available",
    "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
    "REYES | Sergeant | Fitness:79 | Status:available",
]



class Soldier():
    # Attributes 
    def __init__(self, name:str, rank:str, fitness:str, status:str):
        self.rank:str = rank
        self.name:str = name
        self.fitness:int = int(fitness)
        self.deployed:str = status

    def __str__(self):
        print(f'{self.name} ({self.rank}, fitness:{self.fitness}, deployed:{self.deployed})')
    # Methods
    def dispatch(self):
        self.deployed = 'Deployed'

def process_reports(reports:list):
    roster = {}
    ranks = set()

    for report in reports:
        parts = report.split("|")

        name = parts[0].strip().title()
        rank = parts[1].strip().upper()

        fitness_data = parts[2].strip().split(":")
        fitness = int(fitness_data[1].strip())

        status_data = parts[3].strip().split(":")
        status = status_data[1].strip().lower()

        deployed = status == "deployed"

        soldier = Soldier(name, rank, fitness, deployed)

        roster[name] = soldier
        ranks.add(rank)

    return roster, ranks


def show_available(roster:dict):
    available_names = []

    for name in roster:
        if roster[name].deployed == False:
            available_names.append(name)

    available_names.sort()

    print("Available soldiers:", available_names)


def dispatch(roster, name):
    name = name.title()

    if name not in roster:
        print(f"{name} not found.")
    elif roster[name].deployed:
        print(f"{name} is already deployed.")
    else:
        roster[name].dispatch()
        print("Done. Status set to deployed.")


def fitness_report(roster):
    report = {
        "high": [],
        "medium": [],
        "low": []
    }

    for name in roster:
        soldier = roster[name]

        if soldier.fitness >= 80:
            report["high"].append(soldier.name)
        elif soldier.fitness >= 60:
            report["medium"].append(soldier.name)
        else:
            report["low"].append(soldier.name)

    report["high"].sort()
    report["medium"].sort()
    report["low"].sort()

    return report


# Process the reports
roster, ranks = process_reports(reports)

print("=== ROSTER LOADED ===")
print(f"{len(roster)} soldiers on record.")
print("Ranks on file:", ranks)
print()

# Show available soldiers
show_available(roster)
print()

# Dispatch soldiers
print("Dispatching Santos...", end="   ")
dispatch(roster, "Santos")

print("Dispatching Kowalski...", end=" ")
dispatch(roster, "Kowalski")

print()

# Show updated status
print("UPDATED STATUS:")
print(f"  Santos   : {'deployed' if roster['Santos'].deployed else 'available'}")
print(f"  Kowalski : {'deployed' if roster['Kowalski'].deployed else 'available'}")
print()

# Fitness report
print("FITNESS REPORT:")
fitness = fitness_report(roster)

print("High 80+:", fitness["high"])
print("Medium 60-79:", fitness["medium"])
print("Low <60:", fitness["low"])