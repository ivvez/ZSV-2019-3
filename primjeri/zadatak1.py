#1.zadatak
jako_dobri = []
manje_dobri = []
n = int(input("Broj imena"))
for i in range(n):
    ime = input("Upiši znak i ime:")
    ime2 = ime.split(" ")
    if ime2[0] == "+":
        jako_dobri.append(ime2[1])
    else:
        manje_dobri.append(ime2[1])
        
print(jako_dobri)
print(manje_dobri)
