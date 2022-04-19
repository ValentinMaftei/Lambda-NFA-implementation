f = open("date.in", "r")

def validare(cuvant, nod):
    global stareInitiala, stariFinale, automat, traseu, ok
    if nod not in automat:                                      # Verific daca nodul in care am ajuns este sau nu in dictionar
        if nod in stariFinale and cuvant == "":                 # Verific daca nodul in care am ajuns este stare finala si daca nu mai am litere
            traseu.append(nod)                                  # Adaug starea finala in traseu
            ok = 1
    elif cuvant != "":                                          # In cazul in care nu am terminat de prelucrat toate literele
        for listeMici in automat[nod]:                          # Parcurg listele mici de la fiecare stare
            if cuvant[0] == listeMici[1]:                       # Verific daca prima litera din cuvant se afla in una din listele mici
                copie = cuvant[1:]                              # Tai o litera din cuvant
                traseu.append(nod)
                validare(copie, listeMici[0])                   # Lucrez cu cuvantul care are litera eliminata
                if ok == 1:                                     # Verific daca traseul este bun sau trebuie sa ma intorc
                    return None
                traseu.pop()
            if listeMici[1] == '#':                             # Iau cazul cu lambda in care nu trebuie sa sterg litera
                traseu.append(nod)
                validare(cuvant, listeMici[0])
                if ok == 1:                                     # Din nou verific daca traseul este bun sau trebuie sa ma intorc
                    return None
                traseu.pop()


fisier = f.readlines()
nrNod = int(fisier[0].split()[0])       # Memorez numarul de stari
nrTranz = int(fisier[0].split()[1])     # Memorez numarul de tranzitii

i = 1
automat = {}
while i <= nrTranz:
    if fisier[i].split()[0] in automat:
        automat[fisier[i].split()[0]].append([fisier[i].split()[1], fisier[i].split()[2]])
    else:
        automat[fisier[i].split()[0]] = [[fisier[i].split()[1], fisier[i].split()[2]]]
    i += 1

# Construiesc automatul ca un dictionar avand ca chei starile si la fiecare stare am facut o lista
# care sa contina mai multe liste mici unde memorez starile in care pot ajunge si prin ce tranzitii
# {'0': [['1', 'a'], ['2', '#']], '1': [['1', 'b'], ['3', '#']], '2': [['2', 'b'], ['4', 'c']],
# '3': [['5', 'c']], '4': [['5', 'c']]}

stareInitiala = int(fisier[i].split()[0]) # Memorez starea initiala
i += 1

nrStariFinale = int(fisier[i].split()[0])   # Memorez numarul de stari finale
j = 1
stariFinale = []
while j <= nrStariFinale:
    stariFinale.append(fisier[i].split()[j])    # Fac o lista unde memorez starile finale
    j += 1

i += 1
nrCuvinte = int(fisier[i].split()[0])   # Memorez numarul de cuvinte

i += 1
cuv = 1

while cuv <= nrCuvinte:
    ok = 0
    cuvant = fisier[i].strip()          # Memorez string-urile
    stareInitiala = str(stareInitiala)
    if cuvant == "#":                   # Iau cazul in care primesc lambda ca input
        ok = 1
        traseu = [stareInitiala]
    else:
        traseu = []                     # Fac o lista care reprezinta traseul final
        validare(cuvant, stareInitiala)
    cuv += 1
    i += 1
    if (ok == 1):
        print("DA")
        print(traseu)
    else:
        print("NU")
