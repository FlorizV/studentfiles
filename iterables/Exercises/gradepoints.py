# def main():
    #maak een lege dictionary - ditis een oplossing van William:
    # cijfers = {}
    #vul de dictionary via user input met vakken en het cijfer
    # cijfer = int(input('voer het cijfer in voor Engels '))
    # cijfers ['Engels']= cijfer
    # cijfer = int(input('voer het cijfer in voor Wiskunde '))
    # cijfers ['Wiskunde']= cijfer
    # cijfer = int(input('voer het cijfer in voor Algemene studies '))
    # cijfers ['Algemene studies']= cijfer
    # cijfer = int(input('voer het cijfer in voor Kunst '))
    # cijfers ['Kunst']= cijfer
    # cijfer = int(input('voer het cijfer in voor Muziek '))
    # cijfers ['Muziek']= cijfer
    
    #print(cijfers)
    #bereken het gemiddelde cijfer mbv
    #de values(), sum() en len() functies
    # som = (sum(cijfers.values()))
    # aantal = len(cijfers)
    # print(som/aantal)
    # print('Het gemiddelde cijfer is: ',som/aantal)


def main():

    vakkenlijst = {'Engels':0,'Wiskunde':0,'Algemene studies':0,'Kunst':0,'Muziek':0}

    	#dit moet het zijn:
    print(vakkenlijst)
    for vak, cijfer in vakkenlijst.items():
        print('het oorsponkelijke cijfer van', vak, 'was', cijfer )
        vakkenlijst[vak] = int(input('Voer het nieuwe cijfer in voor ' +vak+'? '))
    
    print(vakkenlijst)
    
main()

#sjaaks oplossing:

# def main():
#     vakken = {}
#     vakken['Engels'] = int(8)
#     vakken['Wiskunde'] = int(7)
#     vakken["Aardrijkskunde"] = int(6)
#     vakken["Kunst"] = int(9)
#     vakken["Muziek"] = int(9)

#     punten = vakken.values()

#     gemiddelde = (sum(punten)/len(punten))

#     print("Je gemiddelde cijfer is: ", gemiddelde, "Zou je het cijfer voor Aardrijkskunde willen veranderen naar een 8? ")

#     vakken.update["Aardrijkskunde"] = int(input("Voer hier het nieuwe cijfer in: "))
    
#     print("De cijferlijst is nu weer up-to-date! ", gemiddelde)

# main()