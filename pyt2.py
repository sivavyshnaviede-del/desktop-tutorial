# Sports Tournament Ranking System
# Win = 3 points, Draw = 1 point, Loss = 0 points

teams = ["Tigers", "Eagles", "Lions", "Wolves"]
wins = [3, 2, 2, 1]
draws = [1, 2, 1, 2]
losses = [0, 0, 1, 1]

results = []

for i in range(len(teams)):
    points = wins[i] * 3 + draws[i]
    results.append((teams[i], points, wins[i]))

# Sort by points, then by number of wins
results.sort(key=lambda team: (team[1], team[2]), reverse=True)

print("TOURNAMENT RANKING")
print("Rank  Team       Points  Wins")

for i in range(len(results)):
    team, points, win_count = results[i]
    print(i + 1, team, points, win_count)
