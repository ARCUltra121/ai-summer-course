class Soldier():
    # Attributes 
    def __init__(self, name:str, rank:str, fitness:str, status:str):
        self.rank = rank
        self.name = name
        self.fitness = fitness
        self.deployed = status

    def __str__(self):
        return print(f'{self.name} ({self.rank}, fitness:{self.fitness}, deployed:{self.deployed})')
    # Methods
    def dispatch():
        pass

    