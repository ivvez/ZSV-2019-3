#5.zadatak
a = "OKEILEKOUNDSOOJASLBOEMOJVEDIOLC5ABAOŠOPNIJ!HIJRINOUKEO!"
n = len(a)//5
poruka=""
for i in range(n):
    for j in range(i,len(a),n):
        poruka += a[j]
        
print(poruka)
