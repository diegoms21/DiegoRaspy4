class Operaciones:
    def __init__(self, a , b): #coloco siempre self al inicio, hace referencia al objeto instanciado
        self.num1 = a #si no le coloco el self, la variable num1 solo existe en el metodo constructor init
        self.num2 = b
        self.otro = "Soy otra cosa de ejemplo"
    def suma(self):
        c = self.num1 + self.num2 #c solo existe en este metodo
        return c
    def resta(self):
        c = self.num1 - self.num2
        return c
    def multi(self):
        c = self.num1 * self.num2
        return c
    def divi(self):
        c = self.num1 / self.num2
        return c

print("Inicio de programa")
continuar = True
while continuar:
    dato1 = int(input("digite el numero 1: "))
    dato2 = int(input("digite el numero 2: "))
    if dato1 == "z":
        continuar = False
    else:
        op = Operaciones(dato1,dato2)
        print("La suma es:", op.suma())
        print("La resta es:", op.resta())
        print("La multiplicacion es:", op.multi())
        print("La división es:", op.divi())
        print(op.otro)
print("Fin de programa principal")