# A simple program calculating revenue and expenses of a small coffee shop.
articles_and_prices = {"Bubblegum": 202,
           "Toffee": 118,
           "Ice cream": 2250,
           "Milk chocolate": 1680,
           "Doughnut": 1075,
           "Pancake": 80}

print("Earned amount:")

total_earn = 0

for key, value in articles_and_prices.items():
    total_earn += value
    print(f"{key}: ${value}")

print(f"Income {total_earn}")

staff_expenses = int(input("Staff expenses:\n"))

other_expenses = int(input("Other expenses:\n"))

print(f"Net income:{total_earn - staff_expenses - other_expenses}")