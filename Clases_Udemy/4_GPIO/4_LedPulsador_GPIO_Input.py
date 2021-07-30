#codigo que mientras se enciende un pulsador se enciende el led, y mientras se suelta se
#apaga el led
#Si no presionamos llega un 0 o un LOW al pin, si presionamos llega 3.3V o 1 o HIGH 

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(20,GPIO.IN)

try:
    while True:
        GPIO.output(2, GPIO.input(20)) #escribimos en el GPIO 2 el valor que recibimos en la entrada del pin 20
except:
    GPIO.cleanup()
    print("fin de programa")

'''
try:
    while True:
        if GPIO.input(20) == GPIO.HIGH:
            GPIO.output(2,GPIO.HIGH)
        else:
            GPIO.output(2,GPIO.LOW)
except:
    GPIO.cleanup()
    print("fin de programa")'''