#6. sortiraj listu test(ime,broj bodova, ocjena) po broju bodova od najvece do najmanje vrijednosti 
test = [["Ante Maric", 45, 5],
        ["Marko Anic", 23,2],
        ["Iva Evic", 40, 4],
        ["Eva Buric", 35, 3],
        ["Karla Horvat", 30,2]]

def bodovi(el):
    return el[1]

test.sort(key=bodovi,reverse=True)
for i in test:
    print (i[0],i[1])
