#al usar hilos, ejecuta ambas lineas de codigo, la principal y la del hilo en paralelo
import threading as th #libreria de hilos
import time
a=0
def funcion1():
    global contador
    contador = 0
    while True: 
        time.sleep(1)
        contador += 1
        
#para este ejemplo el hilo es un contador
hilo1= th.Thread(target=funcion1)
hilo1.start()
num=contador
while True:
    if num != contador:
        print(contador)
        num=contador