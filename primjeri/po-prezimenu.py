#5. sortiraj listu imena po prezimenu
imena = ["Josip Peric", "Tina Anic", "Kristina Buric", "Ivan Horvat"]
imena.sort(key=lambda s:s.split()[1])
print(imena)

#s obicnom funkcijom
'''
def prezime(el):
    return el.split()[1]

imena.sort(key=prezime)
print(imena)
    
'''
