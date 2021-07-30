import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setwarnings(False)

continuar = True
while continuar:
    dato = input("Digite la letra de control:")
    if dato == "a":
        GPIO.output(2, GPIO.HIGH)
    elif dato == "b":
        GPIO.output(2, GPIO.LOW)
    elif dato == "z":
        continuar = False
print("fin de programa")
GPIO.cleanup()