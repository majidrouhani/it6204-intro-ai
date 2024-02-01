import random

hemmelig_tall =  random.randint(0, 100)  # Hent et tilfeldig tall

gjettet = 0  # Initier variabelen for gjettet tall
antall_gjettet = 0  # Initier counter for antall forsøk

while gjettet != hemmelig_tall:

    gjettet = int(input('Gjett det hemmelige tallet (1-100): '))  # Ta inn et gjett fra bruker
    antall_gjettet += 1  # Øk antall forsøk med 1 for hver runde

    # Skriv din kode under denne linjen ###
    if hemmelig_tall != gjettet:
        diff = gjettet - hemmelig_tall

        tips = ""
        if diff<0:
            tips = "Prøv med høyere tall"
        else:
            tips = "Prøv med lavere tall"

        print("Gjett på nytt. Tips: ",tips)
    else:
        # Skriv din kode over denne linjen ###
        print('Du gjettet riktig! Det hemmelige tallet var', hemmelig_tall, '. Du brukte', antall_gjettet, 'forsøk.')

