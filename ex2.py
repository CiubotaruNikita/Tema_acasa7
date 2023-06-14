import random

numar_ales = random.randint(1, 100)
numar_incercari = 0
ghicit = False

while not ghicit:
    ghiceste = int(input("Ghiciți numărul: "))
    numar_incercari += 1

    if ghiceste == numar_ales:
        ghicit = True
        print(f"Felicitări! Ați ghicit numărul corect în {numar_incercari} încercări.")
    elif ghiceste < numar_ales:
        print("Mai mare")
    else:
        print("Mai mic")