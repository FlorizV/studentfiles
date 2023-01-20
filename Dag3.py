#programma om even en oneven getallen te laten beweren door computer:
"""
def main ():

    getal=int(input("Voer een getal in en ik vertel of het even of oneven is:"))
    

    rest_waarde = getal%2

    if rest_waarde == 0:
        print(getal,"is een even getal")
    else:
        print(getal,"is een oneven getal")

main()
"""
#dobbelsteen maken met tools uit de random library:
""""
import random
getal = random.randint(1, 6)
print(getal)
"""
#programma om pizza stukken te berekenen en wat er moet besteld worden en wat er daarna rest:
'''
import math

def main():
    
    aantal_mensen = int(input('Hoeveel mensen eten er mee? '))
    stukken_per_persoon = float(input('Hoeveel stukken pizza eet iemand? '))
    stukken_in_een_pizza = int(input('In hoeveel stukken is de pizza gesneden? '))

    totaal_aantal_pizzas = (math.ceil(aantal_mensen * stukken_per_persoon / stukken_in_een_pizza))
    print ('Het aantal pizzas dat besteld moet worden is',totaal_aantal_pizzas)
   
    restaantal = (totaal_aantal_pizzas * stukken_in_een_pizza) - (aantal_mensen * stukken_per_persoon)
    print ('Er zullen nog',restaantal,"stukken overblijven")

main()
'''
#nogmaals hetzelfde programma als hierboven maar dan volledig uitgeschreven in functies en parameters
'''
import math

#
# invoer gegevens
#
def gegevens_invoer():
    aantal_mensen = int(input("Hoeveel mensen eten? "))
    aantal_stukken = float(input("Hoeveel stukken per persoon? "))
    aantal_stukken_in_pizza = int(input("Hoeveel stukken per pizza? "))
    return (aantal_mensen, aantal_stukken,aantal_stukken_in_pizza)
#
# berekening gegevens
#
def bereken_aantal_pizzas(aantal_mensen, aantal_stukken, aantal_stukken_in_pizza):
    totaal_benodigde_stukken = aantal_mensen * aantal_stukken
    benodigde_pizzas = math.ceil(totaal_benodigde_stukken / aantal_stukken_in_pizza)
    overgebleven_stukken = (benodigde_pizzas * aantal_stukken_in_pizza) - totaal_benodigde_stukken
    return (benodigde_pizzas, overgebleven_stukken)

#
# console output
#
def output(benodigde_pizzas, aantal_mensen, overgebleven_stukken):
    print("Je hebt", benodigde_pizzas ,"pizza's nodig om", aantal_mensen ,"mensen te voeden." )
    print('Er zullen nog', overgebleven_stukken ,'stukken overblijven')


def main():
    lijst2 = gegevens_invoer()
    lijst1 = bereken_aantal_pizzas(lijst2[0], lijst2[1], lijst2[2])
    output(lijst1[0],lijst2[0],lijst1[1])

main()
'''
