#condicion que es TRUE o FALSE
# a == b|a > b|a < b|a >= b|a <= b|a != b|
a = int(input("ingrese un numero: "))
b = a%2
if b == 0:
    print("el numero es par")
else:
    print("el numero es impar")