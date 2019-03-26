#2.zadatak
rudolf = ["Ana", "Iva", "Josip", "Tin", "Marin", "Maja"]
djed = ["Josip", "Luka", "Tina", "Ana"]
def dobri(rudolf,djed):
    lista = []
    for i in rudolf:
        if i in djed:
            lista.append(i)
    return (sorted(lista))

print(dobri(rudolf,djed))
