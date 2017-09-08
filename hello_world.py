from random import randrange

pc = randrange(0,3)
human = int(input("Zadej cislo (0,1 nebo 2 "))
kamen = 0
nuzky = 1
papir = 2

if pc == kamen:
    while human != papir:
        if human == kamen:
            print("eště ráz1")
            break

        elif human == nuzky:
            print("skoro1")
            break
        elif human == papir:
            break
    pc = "kamen"
elif pc == papir:
    while human != nuzky:
        if human == papir:
            print("eště ráz2")
            break
        elif human == kamen:
            print("skoro2")
            break
        elif human == nuzky:
            break
    pc = "papir"
elif pc == nuzky:
    while human != kamen:
        if human == nuzky:
            print("eště ráz3")
            break
        elif human == papir:
            print("skoro3")
            break
        elif human == kamen:
            break
        pc = "nuzky"

print("vyhráls, počítač měl",pc)