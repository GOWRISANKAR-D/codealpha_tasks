
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_value = 0
portfolio = []

print("Stock Portfolio Tracker")
print("Available stocks:", list(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        value = stock_prices[stock] * quantity
        total_value += value
        portfolio.append((stock, quantity, value))
    else:
        print("Stock not found!")

print("\n----- Portfolio Summary -----")
for item in portfolio:
    print("Stock:", item[0], "Quantity:", item[1], "Value:", item[2])

print("\nTotal Investment Value:", total_value)


save = input("\nSave result to file? (yes/no): ").lower()

if save == "yes":
    file = open("portfolio.txt", "w")
    file.write("Stock Portfolio Summary\n")
    for item in portfolio:
        file.write(f"{item[0]} {item[1]} {item[2]}\n")
    file.write(f"Total Investment: {total_value}")
    file.close()
    print("Data saved to portfolio.txt")
