def main():
   # Replace this line with your code

    zin = input("Geef aub een zin op: ")
    print("Uw zin is: ",zin)
    getal = int(input("Noem nu een getal: "))
    print("Het teken dat in uw zin op plek nummer",getal, "staat is", zin[getal-1])

main()