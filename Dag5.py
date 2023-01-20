#lijst maken: vierkante haken, begint met tellen bij nul, dit is een lijst met 7 waarden
# namen=[0,1,2,3,4,5,6,7]
#print(namen[0-6]) : dit print waarden die horen bij 1 tot 7
#achteruit tellen, begint bij laatste waarde:
#print(namen[-1])

#dictionaries maak je met accoalades, de waarden staan tussen aanhalingtekens, de combinatie
#die bij waarde 1 hoort staat achter een dubbele punt. De volgende waarde komt na de komma,
#sluit af met accolades.
# vakken = {'wiskunde':8,}
#een dictionary is een lijst met vakjes met waardes en bijbehorende sleutels

#voorbeelden van William van bovenstaande uitleg:

# namen = [7,8,6,5,5,6,7]
# print(namen[2])

# vakken = {'wiskunde':8,
# 'aardrijkskunde':6}

# print(vakken['aardrijkskunde'])

# vakken['engels']=7
# print(vakken)

# vakken['engels']=9
# print(vakken)

# print(vakken.pop('aardrijkskunde'))
# print(vakken.keys())

# print(vakken.values())

# nawlijst = {'jan':{'adres':'vrijheidslaan 2', 'telefoonnr':'088-767364'},
# 'piet':{'adres':'hobbemakade 3', 'telefoonnr':'088-767364'}
# }

# for gegeven in nawlijst.values():
#     print(gegeven['adres'], gegeven['telefoonnr'])

#Objecten en classes
#classes zijn categorieen waar de objecten bijv lid van zijn
#objecten zijn bijv mensen of dingen
#we gaan een class maken: bij classes maken gebruik je een hoofdletter.
#als iets met een kleine letter begint is dit een variabele of een functie

# class Student():
#     klas = 5
#     def __init__(self, naam):
#         self.naam = naam
#         self.adres= ''
#         self.telefoonnummer = ''
#     def layout(self):
#         print('Student', self.naam, 'woont aan', self.adres)

#s1 = Student('Jan')
#s2 = Student('Piet')

# print(s1.klas)
# print(s2.klas)

# print(s1.naam)
# print(s2.naam)

# print(s1.adres)
# print(s2.telefoonnummer)

#s1.adres = 'Hobbemakade 5'

# print(s1.adres)
# print(s2.adres)

#print(s1.layout())
#print(s2.layout())

# class Auto():
#     def __init__(self, merk):
#         self.merk = merk
#         self.snelheid = 0
#         self.kilometerstand = 0
#         self.bouwjaar = 0
#     def rijden(self):
#         self.snelheid = 50

