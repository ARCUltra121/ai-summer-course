import main

class Game():
    def __init__(self, difficulty = "normal"):
        self.difficulty = difficulty

class Spacecraft():
    #Initialization
    def __init__(self, name, fuel_level, fuel_efficiency):
        self.name = name
        self.fuel_level = fuel_level
        self.max_fuel = 200_000
        if main.player.difficulty == 'normal':
            self.fuel_efficiency = fuel_efficiency
        elif main.player.difficulty == 'hard:':
            self.fuel_efficiency = fuel_efficiency / 2
        elif main.player.difficulty == 'easy':
            self.fuel_efficiency = fuel_efficiency * 2
        else:
            raise ValueError('Invalid Game Difficulty')
        
    
    #Methods
    def add_fuel(self, quantity):
        self.fuel_level = min(self.max_fuel, self.fuel_level + quantity)
    def fuel_calculation(self, distance):
        amount = distance / self.fuel_efficiency
        return amount
    def fuel_checker(self, distance):
        return self.fuel_level >= self.fuel_checker(distance)
    def launch_spacecraft(self, distance):
        if self.fuel_checker(distance):
            pass

class Planet():
    #Initialization
    def __init__(self, name, coordinates, danger, resources, atmosphere):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere

    def __str__(self) -> str:
        return f"'Planet: {self.name}\nLocated at coordinates: {self.coordinates}\nDanger level: {self.danger}.\nResources available: {self.resources}\nAtmosphere: {self.atmosphere}'"

    #Methods

class Player():
    #Initialization
    def __init__(self, name, difficulty = "normal"):
        self.name = name
        self.difficulty = difficulty

    #Methods

mars =  Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin")

print(mars.__str__)