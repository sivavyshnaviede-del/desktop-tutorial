# Campus Festival Registration and Financial Audit

registrations = [
    ("ST101", "Anu", 200),
    ("ST102", "Bala", 200),
    ("ST103", "Charan", 200),
    ("ST102", "Bala", 200)  # Example duplicate registration
]

sponsorship = 5000
expenses = [2500, 1200, 800]  # Venue, equipment, refreshments

seen_ids = []
registration_income = 0

for student_id, name, fee in registrations:
    if student_id in seen_ids:
        print("Duplicate registration detected:", student_id)
    else:
        seen_ids.append(student_id)
        registration_income += fee

total_expenses = 0
for expense in expenses:
    total_expenses += expense

total_income = registration_income + sponsorship
balance = total_income - total_expenses

print("\\nFESTIVAL FINANCIAL SUMMARY")
print("Valid registrations:", len(seen_ids))
print("Registration income: Rs.", registration_income)
print("Sponsorship: Rs.", sponsorship)
print("Total income: Rs.", total_income)
print("Total expenses: Rs.", total_expenses)
print("Final balance: Rs.", balance)

if balance > 0:
    print("Result: Surplus")
elif balance < 0:
    print("Result: Deficit")
else:
    print("Result: Break-even")
