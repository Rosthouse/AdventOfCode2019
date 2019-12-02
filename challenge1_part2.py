# Advent of Code 2019: Day 1, Part 2
# https://adventofcode.com/2019/day/1
import math

def calc_fuel(mass):
    fuel = math.floor( mass / 3) - 2
    if(fuel > 0):
        addedFuel = calc_fuel(fuel)
        if(addedFuel >= 0):
            fuel += addedFuel
    return fuel


fuel = calc_fuel(14)
print(fuel)
assert(fuel == 2)

fuel = calc_fuel(100756)
print(fuel)
assert(fuel == 50346)

fuel = calc_fuel(1969)
print(fuel)
assert(fuel == 966)




f = open("./res/challenge1.txt", "r")
lines = f.readlines()
total_fuel = 0
for l in lines:
    mass = int(l)
    fuel = calc_fuel(mass)
    print(fuel)
    total_fuel += fuel

print("Total: " + str(total_fuel))

