import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
pwm = GPIO.PWM(2,500) #T=2ms = 1/500 o 500Hz
pwm.start(0)
flag = True
while flag:
    a = input("ingrese el valor de Dutycycle: ")
    if a == "f":
        flag = False
    else:
        dc=int(a)
        pwm.ChangeDutyCycle(dc)
pwm.stop()
print("fin de programa")