import RPi.GPIO as GPIO
#el servo gira de 0 a 180
#Ton = 0.5ms  | 0 grados   | DC =  2.5
#Ton = 1.5ms  | 90 grados  | DC =  7.5
#Ton = 2.5ms  | 180 grados | DC = 12.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
#GPIO.setwarnings(False)

pwm = GPIO.PWM(2,50) #el servo trabaja con 20ms de perido, que en frecuencia son 50Hzpwm.
pwm.start(2.5) #duty cycle inicial de 2.5

continuar = True
while continuar:
    dato = input("Digite el dc par el servo: ")
    if dato == "z":
        continuar = False
    else:
        pwm.ChangeDutyCycle(float(dato))
pwm.stop()
GPIO.cleanup()
print("Fin de programa")

#Codigo que recibe el dutycycle entre 2.5 y 12.5 que permite mover el eje del robot entre 0 y 180°