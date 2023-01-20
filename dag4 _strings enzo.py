#dit is een string: strings tellen vanaf positie 0, dus de M staat op positie 0
naam = "Monty Python"
#tellen in strings: wat staat er op positie 6?
print (naam[6])
#toon wat er staat op positie 0 tot 5 (dus TOT)!
print(naam[0:5])
#terugtellen in strings begint terug te tellen
print (naam[-5])
print (naam[-3])
#telt hoeveel posities er zijn in een string
print(len(naam))
#je kunt zo ook printen met de f binnen de haken dan hoef je geen plusjes te gebruiken en geen spatie te tellen
begroeting ='Hallo'
naam = 'Monty python'
print(f'{begroeting} {naam} hoe gaat het?')
print(begroeting+naam)
print(begroeting," ",naam)
#lists maken: als je rechte haken gebruikt maak je een lijst, ga boven de var hangen zie je list
colors = ["red","blue","green","orange"]
print(colors[2])
#sorteren van lists na regel 26 staan de namen opeens op alfabet
naam1 = "boudewijn"
naam2 = "albert"
namen = [naam1,naam2]
print(namen)
namen.sort()
print(namen)
#lijst met vierkant haken is een lijst die je kan bewerken, zo'n lijst wordt ook wel een array genoemd
#lijsten met ronde haken zijn niet meer aan te passen, dit wordt een tuple genoemd, kan veiliger zijn
#of hoeven niet voor de verwerking te worden bewerkt dus onveranderbaar.
#range is een reeks in een lijst heeft de vorm: range(1,100) dit houdt het begin de de stop van de reeks in.

#loop: hier wordt de lijst van kolom1 weergegeven met print. Het woord for is een zgn
#for-loop
kolom1=['william','susan','dennes','bjorn']
kolom2=['0529-4545','12354','6734874','87997714']
for item in kolom1:
    print(item)

# import random Dit importeert de random(functie?) waardoor de machine willekeurige items kiest

import random

kolom1 = ['William','Susan','Dennes','Bjorn']
kolom2 = ['06-652362','088-8716287','055-232','0900-1212']

tabel = [kolom1, kolom2]

for item in range(1,10):
    naam = random.choice(kolom1)
    print(naam)

#Naast for loop (je weet hoe lang je gaat loopen, Je hebt ook nog zoiets als een while loop)
num=0
while num <6:
    print(num)
    num += 1
#ander voorbeeld while loop: een soort wachtwoord checker, hij blijft loopen tot 12345 de imput is
paswoord = input ('voer wachtwoord in: ')
wachtwoord = '12345'
    # !=  <=dit betekent ongelijk aan
    # ==  dit betekent gelijk aan
while paswoord != wachtwoord:
    paswoord = input ('voer wachtwoord in: ')
# oefening met een while loop
namen = []
naam = input("Voer een naam in: ")

while naam:
    namen.append(naam)
    if naam == "":
        break #zo ga je uit deze loop
for naam in namen:
    print(naam)