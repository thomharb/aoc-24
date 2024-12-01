raw = open('input.txt').readlines()

left = sorted([int(x.split()[0]) for x in raw])
right = sorted([int(x.split()[1]) for x in raw])

print(sum([abs(left[i] - right[i]) for i in range(len(left))]))
