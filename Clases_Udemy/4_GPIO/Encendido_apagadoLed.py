import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.LOW)
bandera=True
while (bandera==True):
    letra = input("Ingrese una letra: ")
    if letra == "a":
        GPIO.output(2,GPIO.HIGH)
    elif letra == "b":
        GPIO.output(2,GPIO.LOW)
    elif letra == "z":
        bandera = False
    else:
        print("Digite una letra correcta, a,b o z")
print("Programa finalizado")