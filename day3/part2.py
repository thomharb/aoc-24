import re

raw = open("input.txt").read()

total = 0
mul = True

for m in re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", raw):
    if m.startswith("mul") and mul:
        total += [int(x) for x in (m[4:len(m) - 1]).split(",")][0] * [int(x) for x in (m[4:len(m) - 1]).split(",")][1]
    elif m.startswith("don't"):
        mul = False
    elif m.startswith("do"):
        mul = True
print(total)
