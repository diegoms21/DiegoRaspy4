import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.output(2,GPIO.LOW)

try:
    while True:
        GPIO.output(2,GPIO.HIGH)
        time.sleep(0.00001) #envia un pulso cada 10 microsegundos o 0.00001 seg
        GPIO.output(2,GPIO.LOW)
        t1 = time.time()
        while GPIO.input(20) == GPIO.LOW: #el echo vale 0, vamos a esperar a que valga 1
            t1 = time.time() #si todavia vale 0 hay que actualizar el t1 con el tiempo
            #recién cuando la entrada está en alto es que salimos del while y entramos al siguiente
        while GPIO.input(20) == GPIO.HIGH: #esperaremos acá mientras la entrada esté en alta
            t2 = time.time() #recien cuando esté en baja nuevamente saldremos de aca
        
        '''DIFERENCIA DE TIEMPO'''
        t = t2 - t1
        d = 17000 * t
        print("distancia: ", round(d,1), "cm") #round redondea los decimales a los que ponga, ahora 1 decimal
        time.sleep(0.2)
except: #salimos con Ctrl C del programa
    GPIO.cleanup()
    print("fin de programa")
    