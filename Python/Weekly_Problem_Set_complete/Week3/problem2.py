import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def orbit_circumference(radius):
    return 2 * math.pi * radius

def fuel_needed(mass,velocity):
    return math.floor(0.5 * mass * velocity ** 2)



ship_pos = (0, 0)
station_pos = (143, 892)
orbit_radius = 6371
ship_mass = 50000
ship_velocity = 7800


distance_to_station = distance(
    ship_pos[0], ship_pos[1],
    station_pos[0], station_pos[1]
)

circumference = orbit_circumference(orbit_radius)
kinetic_energy = fuel_needed(ship_mass, ship_velocity)

log_velocity = math.log(ship_velocity, 10)


print("=== NAVIGATION REPORT ===")
print(f"Distance to station:    {distance_to_station:.2f} units")
print(f"Orbit circumference:    {circumference:.2f} km")
print(f"Kinetic energy (fuel):  {kinetic_energy} J")
print(f"Log10 of velocity:      {log_velocity:.2f}")