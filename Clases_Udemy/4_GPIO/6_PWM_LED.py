import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

#EL PIN GPIO2 le asignamos 500Hz de frecuencia (f) o lo mismo que 2ms de periodo (T)
#para apreciar el cambio de intensidad en un led se recomienda T=2ms
pwm = GPIO.PWM(2,500)
pwm.start(0) #le damos el dutycytle de 0%

continuar = True:
    while continuar:
        dato = input("Digite un nuevo DC:" )
        if dato == "z":
            continuar = False
        else:
            pwm.ChangeDutyCycle(int(dato))
pwm.stop()
GPIO.cleanup()
print("fin de programa")