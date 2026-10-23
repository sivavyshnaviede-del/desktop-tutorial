# Energy Conservation Before-and-After Analysis

appliances = ["Lights", "Fans", "Air conditioner", "Computers"]
before = [30, 45, 120, 60]
after = [20, 35, 90, 48]

savings = []

print("ENERGY CONSERVATION REPORT")

for i in range(len(appliances)):
    saved = before[i] - after[i]
    if before[i] > 0:
        percentage = (saved / before[i]) * 100
    else:
        percentage = 0

    savings.append((appliances[i], saved, percentage))
    print("\\nAppliance:", appliances[i])
    print("Before:", before[i], "kWh")
    print("After:", after[i], "kWh")
    print("Energy saved:", saved, "kWh")
    print("Savings:", round(percentage, 2), "%")

savings.sort(key=lambda item: item[1], reverse=True)
print("\\nAppliance with highest energy saving:", savings[0][0])
