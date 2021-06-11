import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,False)
while True:
    a=int(input('agrega entrada'))
    if a==2:
        GPIO.output(4,True)
    else:
        GPIO.output(4,False)