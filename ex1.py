numar = int(input("Introduceți un număr întreg pozitiv: "))

if numar < 0:
    print("Numărul trebuie să fie pozitiv.")
elif numar == 0:
    print("Factorialul lui 0 este 1.")
else:
    factorial = 1
    while numar > 0:
        factorial *= numar
        numar -= 1
    print("Factorialul este:", factorial)