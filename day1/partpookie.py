lijstje = open("input.txt").readlines()

lijst_met_waarden1 = []
lijst_met_waarden2 = []
getal = 0

for i in range(len(lijstje)):
    tijdelijk_lijstje = lijstje[i].split()
    lijst_met_waarden1.append(int(tijdelijk_lijstje[0]))
    lijst_met_waarden2.append(int(tijdelijk_lijstje[1]))

sorted_lijst_met_waarde1 = sorted(lijst_met_waarden1)
sorted_lijst_met_waarde2 = sorted(lijst_met_waarden2)

for i in range(len(lijstje)):
    getal += abs(sorted_lijst_met_waarde1[i] - sorted_lijst_met_waarde2[i])

print(getal)
