'''instalación: sudo pip3 install Adafruit_DHT'''

import Adafruit_DHT as dht

sensor = dht.DHT11 #DHT22 tambien puede ser
continuar = True
while continuar:
    dato = input("digite algo para leer el sensor:" )
    if dato == "z":
        continuar = False
    else:
        h,t = dht.read_retry(sensor,4) #por defecto viene configurado en BCM, aca está el GPIO4
        print("T = ", t, " H = ", h)
print("fin de programa")

#hay que modificar la libreria, en el video del curso están los pasos