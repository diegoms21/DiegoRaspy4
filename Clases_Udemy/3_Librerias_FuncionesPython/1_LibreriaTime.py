import time
#time.sleep(segundos) genera un retardo dependiendo de la cantidad de segundos que le coloquemos
#while True:
 #   print("ya pasó medio segundo")
  #  time.sleep(0.5)
#time.time() genera la cantidad de segundos desde enero de 1970
#print(time.time()) 

t1 = time.time() #setea el tiempo inicial
t2 = time.time() #tiempo que cambiará
while True:
    if (t2-t1) < 1: #se queda hasta que la diferencia sea menor a 1 segundo
        t2 = time.time() #actualizamos el tiempo que va subiendo
    else: #si llegó al segundo actualiza el t1 y lanza que ya pasó 1 segundo 
        t1 = time.time()
        print("ya paso 1 segundo")