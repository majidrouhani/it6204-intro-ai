tall_liste = []

while True:

    try:
        regnestykke = input("Skriv inn regnestykke på formen x/y: ")

        if regnestykke.upper() == 'Q':
            break  # avslutt

        divident, divisor = regnestykke.split('/')

        tall_liste.append((divident, divisor, float(divident)/float(divisor)))

    except ValueError:
        print("Vennligst oppgi regnestykke på formen x/y, der x og y er tall (heltall, flyttall) F.eks. 10/2")

    except ZeroDivisionError:
        print("Divisor kan ikke være 0!")

print("Du har skrevet " + str(len(tall_liste)) + " regnestykker!")

for i in range(len(tall_liste)):
    print(tall_liste[i][0], "/", tall_liste[i][1], "=", tall_liste[i][2])
