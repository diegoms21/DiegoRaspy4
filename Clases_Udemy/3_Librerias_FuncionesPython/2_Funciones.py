def suma (a,b):
    c = a + b
    return c
def resta (a,b):
    c = a - b
    return c
def ejemplo(*args): #funcion que recibe cantidad indeterminada de argumentos y los imprime
    for i in args:
        print(i)
def suma2(*args):
    total = 0
    for i in args: #recorro todos los argumentos que le paso (con i) y los sumo con total (suma acumulada)
        total = total + i
    return total
def ejemplo2(**kargs): #Usa punteros, permite imprimir listas o tuplas completas
    print (kargs)
    
num1 = int(input("digite el numero 1 :"))
num2 = int(input("digite el numero 2 :"))
print("La suma2 es:" , suma2(num1,num2,2,1,3))
print("La resta es:" , resta(num1,num2))
ejemplo("Diego",25,"Masculino", "peruano", True)
ejemplo2(nombre="Diego",edad="24",sexo="Masculino",licencia=True)