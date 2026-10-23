# Multi-Criteria Internship Candidate Ranking

candidates = [
    ("Anu", 85, 90, 95),
    ("Bala", 92, 80, 88),
    ("Charan", 76, 85, 90),
    ("Divya", 88, 92, 80)
]
# Each tuple: (name, marks, assessment score, attendance percentage)

eligible = []

for name, marks, assessment, attendance in candidates:
    if marks >= 60 and assessment >= 50 and attendance >= 75:
        total = marks + assessment + attendance
        eligible.append((name, total, marks, assessment))
    else:
        print(name, "is not eligible.")

eligible.sort(key=lambda candidate: (candidate[1], candidate[2], candidate[3]), reverse=True)

print("\\nINTERNSHIP CANDIDATE RANKING")
for i in range(len(eligible)):
    name, total, marks, assessment = eligible[i]
    print("Rank:", i + 1, "| Name:", name, "| Total score:", total)
