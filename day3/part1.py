import re

raw = open("input.txt").read()

total = 0

for m in re.findall(r"mul\(\d+,\d+\)", raw):
    total += [int(x) for x in (m[4:len(m) - 1]).split(",")][0] * [int(x) for x in (m[4:len(m) - 1]).split(",")][1]
print(total)
