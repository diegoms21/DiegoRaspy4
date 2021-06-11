import paho.mqtt.client as mqtt
import threading as th
import RPi.GPIO as GPIO

cliente = mqtt.Client()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.output(4,False)
cliente.connect("musach.tk",1883)
def escuchar (cliente, userdata, mensaje):
    sw1 = format(mensaje.payload.decode("utf-8"))    
    print(sw1)
    if sw1=='on':
        GPIO.output(4,True)
    elif sw1=='off':
        GPIO.output(4,False)
    #GPIO.output(4,True)
    
def escuchar2 (cliente,usardata,mensaje2):
    sw2 = format(mensaje2.payload.decode("utf-8"))
    print(sw2)
def escuchar3 (cliente,usardata,mensaje3):
    sw3 = format(mensaje3.payload.decode("utf-8"))
    print(sw3)
def escuchar4 (cliente,usardata,mensaje4):
    sw4 = format(mensaje4.payload.decode("utf-8"))
    print(sw4)
def escuchar5 (cliente,usardata,mensaje5):
    sw5 = format(mensaje5.payload.decode("utf-8"))
    print(sw5)
def escuchar6 (cliente,usardata,mensaje6):
    sw6 = format(mensaje6.payload.decode("utf-8"))
    print(sw6)
cliente.on_message = escuchar
cliente.on_message = escuchar2
cliente.on_message = escuchar3
cliente.on_message = escuchar4
cliente.on_message = escuchar5
cliente.on_message = escuchar6
cliente.subscribe("led1")
cliente.subscribe("led2")
cliente.subscribe("led3")
cliente.subscribe("led4")
cliente.subscribe("led5")
cliente.subscribe("led6")

cliente.loop_forever()
