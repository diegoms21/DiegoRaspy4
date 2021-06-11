import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
while True:
    GPIO.output(2,GPIO.HIGH)
    time.sleep(0.02)
    GPIO.output(2,GPIO.LOW)
    time.sleep(0.02)
print("fin de programa")