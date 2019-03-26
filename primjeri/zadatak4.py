sobovi = ["Dasher Disney", "Dancer Moore", "Prancer Jones", 
          "Vixen Hall", "Comet Smith", "Cupid Knight", "Donder Taylor", 
          "Blitzen Claus" ]
sobovi2 = sorted(sobovi, key=lambda s:s.split()[1])
print(sobovi2)

'''
#funkcija:
def prezime(el):
    b = el.split()
    return b[1]
sobovi2 = sorted(sobovi, key=prezime)
'''
