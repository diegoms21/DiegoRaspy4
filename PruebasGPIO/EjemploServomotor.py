import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
p = GPIO.PWM(4,50) #20ms de periodo es a 50Hz
p.start(7.5)
flag = True
while flag:
    a = input("Ingrese el dutycycle: ")
    if a == "fin":
        flag = False
    else:
        p.ChangeDutyCycle(float(a))
print("Fin de programa")
    
    