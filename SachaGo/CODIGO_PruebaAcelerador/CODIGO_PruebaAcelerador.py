import RPi.GPIO as GPIO
import time
#import serial
#s = serial.Serial("/dev/ttyS0",9600)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT) #S0
GPIO.setup(20, GPIO.OUT) #S1
GPIO.setup(21, GPIO.OUT) #S2

def Encendido(num):
    GPIO.output(num,GPIO.HIGH)
def Apagado(num):
    GPIO.output(num,GPIO.LOW)
    
while True:
    msj = input("digite una letra: ")
    if msj == "a":
        Apagado(18) #0
        Apagado(20) #0
        Apagado(21) #0
        print(msj)
    elif msj == "b":
        Encendido(18) #1
        Apagado(20)   #0
        Apagado(21)   #0
        print(msj)
    #Encendido(18)
    #time.sleep(0.02)
    #Apagado(18)
    #time.sleep(0.02)
    
