import threading as th
import time

def paralelo():
    global contador #con global creo una variable global que funcione afuera de la función
    global conti
    contador = 0
    conti = True
    while conti:
        time.sleep(1)
        contador += 1 #contador = contador + 1
    print("Fin de hilo")

    
print("incio de programa")
hilo = th.Thread(target=paralelo) #creamos el hilo y le asignamos la funcion a correr con el target
hilo.start()
continuar = True
while continuar:
    dato = input("Digite algo: ")
    if dato == "a":
        print(contador)
    elif dato == "z":
        continuar = False
        conti = False
    else:
        print(dato)
print("fin de programa")

#La función paralelo se estará ejecutando cuando iniciemos el hilo, lo unico que hace la función es sumar un contador
#cada segundo mientras esté en el while y conti sea verdadero. Mientras tanto, en la función principal se pide
#ingresar datos, "a" para imprimir el contador, o "z" para cambiar el valor a False de conti y continuar 