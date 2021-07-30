#instalar libreria bluedot
import bluedot.brcomn import BluetoothServer
import RPi.GPIO as GPIO

def leer(data):
    print(data)
    if data == "F":
        GPIO.output(2,GPIO.HIGH)
    elif data == "B":
        GPIO.output(2,GPIO.LOW)
    
'''GPIO'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

print("iniciando servidor Bluetooth")
s = BluetoothServer(leer) #funcion que iremos cuando recibamos informacion, ahora es funcion leer
#crea un hilo y va a esa función cada vez que se reciban datos