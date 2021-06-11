import paho.mqtt.client as mqtt
import threading as th
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
cliente = mqtt.Client()
GPIO.setmode(GPIO.BCM)
GPIO.setup (4, GPIO.OUT)
GPIO.setup (26, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
cliente.connect("musach.tk",1883)
def escuchar (cliente,userdata,mensaje):
    sw1 = format(mensaje.payload.decode("utf-8"))
    print(sw1)
def led(sw1):
    while True:
        if sw1 == "on":
            GPIO.output(4,GPIO.HIGH)
        else:
            GPIO.output(26,GPIO.LOW)
        print ("llego")
cliente.on_message = escuchar
hilo1 = th.Thread(target=led, args=(sw1,))
th.append(hilo1)
hilo1.start()
cliente.subscribe("led1")
cliente.loop_forever
