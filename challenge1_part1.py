import math

f = open("./res/challenge1.txt", "r")
lines = f.readlines()
total_fuel = 0
for l in lines:
    mass = int(l)
    fuel = math.floor(mass / 3) - 2
    print(fuel)
    total_fuel += fuel

print(total_fuel)

