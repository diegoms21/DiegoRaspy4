import RPi.GPIO as GPIO
import time
#import serial
#s = serial.Serial("/dev/ttyS0",9600)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT) #S0
GPIO.setup(16, GPIO.OUT) #S1
GPIO.setup(20, GPIO.OUT) #S2

def Encendido(num):
    GPIO.output(num,GPIO.HIGH)
def Apagado(num):
    GPIO.output(num,GPIO.LOW)
    
while True:
    msj = input("digite una letra: ")
    if msj == "a": #0
        Apagado(18) #0
        Apagado(16) #0
        Apagado(20) #0
        print(msj)
    elif msj == "b": #1
        Encendido(18) #1
        Apagado(16)   #0
        Apagado(20)   #0
        print(msj)
    elif msj == "c": #2
        Apagado(18)   #0
        Encendido(16) #1
        Apagado(20)   #0
        print(msj)
    elif msj == "d": #3
        Encendido(18) #1
        Encendido(16) #1
        Apagado(20)   #0
        print(msj)
    elif msj == "e": #4
        Apagado(18)   #0
        Apagado(16)   #0
        Encendido(20) #1
        print(msj)
    elif msj == "f": #5
        Encendido(18) #1
        Apagado(16)   #0
        Encendido(20) #1
        print(msj)
    elif msj == "g": #6
        Apagado(18)   #0
        Encendido(16) #1
        Encendido(20) #1
        print(msj)
    elif msj == "h": #7
        Encendido(18) #1
        Encendido(16) #1
        Encendido(20) #1
        print(msj)
