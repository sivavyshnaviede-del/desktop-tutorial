# Library Borrowing and Fine Reconciliation

records = [
    ("B101", "Python Basics", 2),
    ("B102", "Web Development", 0),
    ("B103", "Computer Networks", 5),
    ("B104", "Artificial Intelligence", 1)
]

allowed_days = 14
fine_per_day = 5

print("LIBRARY FINE REPORT")

for book_id, title, overdue_days in records:
    if overdue_days > 0:
        fine = overdue_days * fine_per_day
        status = "Overdue"
    else:
        fine = 0
        status = "Returned on time"

    print("\\nBook ID:", book_id)
    print("Title:", title)
    print("Overdue days:", overdue_days)
    print("Fine: Rs.", fine)
    print("Status:", status)
