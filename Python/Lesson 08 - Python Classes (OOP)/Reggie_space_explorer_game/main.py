import objects

player_name: str = input('What is your name Pilot?: ')
game_difficulty: str = input("Please set the game difficulty (Easy, Normal, Hard): ").lower()

player = objects.Player(game_difficulty)

player_spacecraft = objects.Spacecraft("Vostok 1", 250, 1.5)

earth = objects.Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like")