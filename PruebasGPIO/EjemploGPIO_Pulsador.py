import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
#GPIO.setup(20,GPIO.IN,GPIO.PUD_DOWN) para pulldown interno
GPIO.setup(20,GPIO.IN)
while True:
    GPIO.output(2,GPIO.input(20)) #si presiono el pulsador, el puerto 20 lee 3.3V y prende el led
    #si presiono el pulsador, prendo el led, sino se apaga el led
print("Fin programa")

'''while True:
    if GPIO.input(20) == GPIO.HIGH:
        GPIO.output(2,GPIO.HIGH)
    else:
        GPIO.output(2,GPIO.LOW)
print("Fin programa")'''
#Todo esto es un arreglo pull down
