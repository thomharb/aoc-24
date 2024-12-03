raw = open("input.txt").readlines()

safe = 0
for row in raw:
    r = [int(x) for x in row.split()]

    diffs = []
    for i in range(len(r) - 2):
        diffs.append(r[i] - r[i + 1])

    if all(d > 0 for d in diffs) or all(d < 0 for d in diffs):
        if all(1 <= abs(b) <= 3 for b in diffs):
            safe += 1
print(safe)
