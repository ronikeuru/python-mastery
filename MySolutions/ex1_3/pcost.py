# pcost.py

total_cost = 0.0

with open('../../Data/portfolio.dat', mode='r') as f:
    for line in f:
        stock = line.split()

        n, price = float(stock[1]), float(stock[2])

        total_cost += n*price

print("Total cost: ", total_cost, "$")