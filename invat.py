try:
    a = float(input("number1: "))
    x = float(input("number2: "))
    operatie = input("Alege operatie: +, -, /, *,")

    if operatie == "+":
        Rezultat = a + x
        print(f"Rezultat = {Rezultat}")

    if operatie == "-":
        Rezultat = a - x
        print(f"Rezultat = {Rezultat}")
    else:
        if operatie ==  "/":
            if a == 0 or x == 0:
                print("You can't divide by 0")
            else:
                Rezultat = a / x
                print(f"Rezultat = {Rezultat}")

        if operatie == "*":
            if a == 0 or x == 0:
                print("You can't multiply by 0")
            else:
                Rezultat = a * x
                print(f"Rezultat = {Rezultat}")

    print("Congrats")
except:
    print("This doesn't work")