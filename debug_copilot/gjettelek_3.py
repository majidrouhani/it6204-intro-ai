import random

hemmelig_tall = random.randint(0, 100)  # Hent et tilfeldig tall

gjettet = None  # Initier variabelen for gjettet tall
antall_gjettet = 0  # Initier counter for antall forsøk

while gjettet != hemmelig_tall:
    try:
        # Ta inn et gjett fra bruker
        gjettet = int(input('Gjett det hemmelige tallet (0-100): '))
    except ValueError:
        print("Ugyldig inndata. Vennligst skriv inn et heltall.")
        continue

    antall_gjettet += 1  # Øk antall forsøk med 1 for hver runde

    if hemmelig_tall != gjettet:
        tips = "Prøv med høyere tall" if gjettet < hemmelig_tall else "Prøv med lavere tall"
        print("Gjett på nytt. Tips: ", tips)
    else:
        print('Du gjettet riktig! Det hemmelige tallet var',
              hemmelig_tall, '. Du brukte', antall_gjettet, 'forsøk.')
        break
