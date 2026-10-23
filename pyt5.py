# Courier Charge Optimization
# Sample charges are illustrative.

weight = float(input("Enter parcel weight in kg: "))
distance = float(input("Enter delivery distance in km: "))
urgent = input("Urgent delivery? (yes/no): ").lower()

if weight <= 0 or distance <= 0:
    print("Weight and distance must be positive.")
else:
    # Base fee plus weight and distance charges
    standard = 40 + weight * 12 + distance * 2

    if weight > 20:
        standard += 100

    if urgent == "yes":
        express = standard + 80
    else:
        express = standard + 30

    print("\\nStandard delivery: Rs.", round(standard, 2))
    print("Express delivery: Rs.", round(express, 2))

    if standard <= express:
        print("Cheapest option: Standard delivery")
    else:
        print("Cheapest option: Express delivery")

