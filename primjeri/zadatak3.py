#3. zadatak
planeti = [
    #naziv, polumjer, udaljenost Zemlja-Sunce
    ["Merkur",2440, 0.395],
    ["Venera", 6052, 0.723],
    ["Zemlja", 6370, 1.000],
    ["Mars", 3396, 1.530],
    ["Jupiter",71492, 5.210],
    ["Saturn",60268, 9.551],
    ["Uran",25559, 19.213],
    ["Neptun",26764,30.070] 
]
planeti.sort(key=lambda s:s[1])
for i in planeti:
    print (i[0])

'''
#funkcija
def velicina(el):
    return el[1]

planeti.sort(key=velicina)
'''
