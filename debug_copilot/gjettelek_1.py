import random

# Initier variabelen for gjettet tall
Bruker_Gjettet=0
# Initier teller for antall forsøk
antall_bruker_gjettet = 0
# Generer et tilfeldig tall mellom 0 og 100
# og lagre det i variabelen hemmelig_tall
hemmelig_tall = float(random.randint(0, 100))  # Hent et tilfeldig tall

while Bruker_Gjettet != hemmelig_tall:

    # Ta inn et gjett fra bruker
    Bruker_Gjettet = int(input('Gjett det hemmelige tallet (1-100): '))
    antall_bruker_gjettet += 1  # Øk antall forsøk med 1 for hver runde

    # Skriv din kode under denne linjen ###
    if hemmelig_tall != Bruker_Gjettet:
        print("Gjett på nytt")
    else:
        # Skriv din kode over denne linjen ###
        print('Du gjettet riktig! Det hemmelige tallet var',
              hemmelig_tall, '. Du brukte', antall_bruker_gjettet, 'forsøk.')
