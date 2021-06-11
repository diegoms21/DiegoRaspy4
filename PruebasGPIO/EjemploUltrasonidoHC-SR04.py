import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT) #PARA EL TRIGGER
GPIO.setup(20,GPIO.IN) #PARA EL ECHO
GPIO.setwarning(False)
GPIO.output(2,GPIO.LOW)
#time.time() es una funcion que mide el tiempo desde que se inicio la raspberry hasta cuando lo llaman
while True:
    GPIO.output(2,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(2,GPIO.LOW)
    inicio=time.time()
    while GPIO.input(20) == GPIO.LOW: #mientras que el echo vale 0 se queda
        inicio = time.time() #tiempo desde q inicio la raspberry hasta q echo vale 1, inicio la onda sonora
    while GPIO.input(20) == GPIO.HIGH: #mientras que el echo vale 1 se queda
        fin = time.time() #tiempo desde que inicio la raspberry hasta que el echo vale 0, regreso la onda sonora
    rango = fin - inicio
    #distancia = velocid*tiempo--> velocidad sonido = 340m/s y rango es 2 veces la distancia
    #2d=rango*34000(cm/s)
    distancia = rango*17000 #distancia en cm
    print("distancia: ",round(distancia)," cm") #redondea la distancia a un entero
    time.sleep(0.5) #cada 0.5s hace el muestreo