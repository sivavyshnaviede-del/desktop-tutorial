# E-Commerce Order Processing and Reconciliation

products = ["Notebook", "Pen", "Bag"]
prices = [50, 10, 500]
ordered = [4, 10, 2]
returned = [1, 2, 0]
stock = [20, 50, 10]

total_revenue = 0

print("E-COMMERCE ORDER REPORT")

for i in range(len(products)):
    if returned[i] < 0 or returned[i] > ordered[i]:
        print("Invalid return quantity for", products[i])
        continue

    sold = ordered[i] - returned[i]
    amount = sold * prices[i]

    if amount >= 1000:
        discount = amount * 0.10
    elif amount >= 500:
        discount = amount * 0.05
    else:
        discount = 0

    final_amount = amount - discount
    remaining_stock = stock[i] - sold
    total_revenue += final_amount

    print("\\nProduct:", products[i])
    print("Units sold after returns:", sold)
    print("Discount: Rs.", round(discount, 2))
    print("Final amount: Rs.", round(final_amount, 2))
    print("Remaining stock:", remaining_stock)

    if remaining_stock < 0:
        print("Warning: Stock shortage!")

print("\\nTotal revenue: Rs.", round(total_revenue, 2))
