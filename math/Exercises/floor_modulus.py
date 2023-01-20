# write the divide() function
def divide(num1,num2):
    antwoord=num1//num2
    modulo=num1%num2
    print(num1,"gedeeld door",num2,"is gelijk aan",antwoord,"met een rest van",modulo)

def main():
    divide(5, 2)
    divide(6, 3)
    divide(12, 5)
    divide(1, 2)

main()

