brojevi = [5, 8, 4, 12, 9, 1]

for i in range(len(brojevi)-1,0,-1):
    naj = 0
    for j in range(1, i+1):
        # usporedi trenutnu najvecu vrijednost i sljedeci element niza
        if brojevi[j] > brojevi[naj]: 
            naj = j

    #zamjena
    brojevi[i], brojevi[naj] = brojevi[naj], brojevi[i]

print(brojevi)
