# Nested Loop Calendar Generator
# Weekday: 0 = Monday, 1 = Tuesday, ..., 6 = Sunday

month = input("Enter month name: ")
days = int(input("Enter number of days (28 to 31): "))
start_day = int(input("Starting weekday (0=Mon, 6=Sun): "))

if days < 28 or days > 31 or start_day < 0 or start_day > 6:
    print("Invalid input.")
else:
    print("\\n", month)
    print("Mon Tue Wed Thu Fri Sat Sun")

    day = 1
    position = 0

    # Print spaces before the first day
    for i in range(start_day):
        print("    ", end="")
        position += 1

    while day <= days:
        print("%3d " % day, end="")
        position += 1
        day += 1

        if position == 7:
            print()
            position = 0

    if position != 0:
        print()
