"""
3. Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?
`create function: solve(numheads, numlegs):`"""

def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        total_legs = 2 * num_chickens + 4 * num_rabbits
        if total_legs == numlegs:
            return num_chickens, num_rabbits
    return None

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
if result:
    chickens, rabbits = result
    print(result)
else:
    print("No solution found.")