# Environmental Monitoring Data Analyzer
# Example readings are illustrative, not official safety measurements.

locations = ["Campus Gate", "Library", "Laboratory", "Canteen"]
readings = [45, 62, 38, 75]

threshold = 60
total = 0

print("ENVIRONMENTAL MONITORING REPORT")

for i in range(len(locations)):
    value = readings[i]
    total += value

    print("\\nLocation:", locations[i])
    print("Reading:", value)

    if value <= threshold:
        print("Category: Within the example threshold")
    else:
        print("Category: Above the example threshold")

average = total / len(readings)
print("\\nAverage reading:", round(average, 2))

highest_index = readings.index(max(readings))
print("Highest reading location:", locations[highest_index])
