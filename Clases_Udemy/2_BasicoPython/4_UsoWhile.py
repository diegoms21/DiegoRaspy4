inicio = True
while inicio:
    a = input ("ingrese un numero: ")
    if a == "fin":
        inicio = False
    else:
        b = int(a)%2
        if b == 0:
            print("el numero es par")
        else:
            print("el numero es impar")
print("fin de programa")