# Warehouse Inventory Reconciliation

products = ["Laptop", "Mouse", "Keyboard"]
opening_stock = [20, 50, 30]
incoming_stock = [10, 20, 15]
dispatched_stock = [18, 35, 25]
actual_closing_stock = [12, 34, 20]

print("WAREHOUSE INVENTORY REPORT")
print("-" * 65)

for i in range(len(products)):
    expected = opening_stock[i] + incoming_stock[i] - dispatched_stock[i]
    difference = actual_closing_stock[i] - expected

    print("\\nProduct:", products[i])
    print("Expected closing stock:", expected)
    print("Actual closing stock:", actual_closing_stock[i])

    if difference == 0:
        print("Status: Stock matches")
    elif difference < 0:
        print("Status: Shortage of", abs(difference), "units")
    else:
        print("Status: Surplus of", difference, "units")

    if actual_closing_stock[i] < 10:
        print("Reorder alert: Stock is low")
