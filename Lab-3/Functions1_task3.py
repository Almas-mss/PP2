def solve(numheads, numlegs):
    x = (4 * numheads - numlegs) // 2
    y = numheads - x
    if y >= 0 and x >= 0 and 2 * x + 4 * y == numlegs:
        print(f"Chickens: {x}, Rabbits: {y}")
    else:
        print("No solution")
solve(35,94)