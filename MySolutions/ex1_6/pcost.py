# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0
    
    with open(f'../../{filename}', mode='r') as f:
        for line in f:
            stock = line.split()

            try:
                n = int(stock[1])
                price = float(stock[2])
                total_cost += n*price
            except ValueError as e:
                print(f'Couldn\'t parse: {repr(line)}')
                print(f'Reason: {e}')

    return total_cost

if __name__ == '__main__':
    print(f'Total Cost: {portfolio_cost("Data/portfolio3.dat")}$')