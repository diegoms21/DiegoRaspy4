import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import serial

s = serial.Serial("/dev/ttyACM0",9600)

'''Declaración de Salidas GPIO'''
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
# GPIO.setup(,GPIO.OUT)
# GPIO.setup(,GPIO.OUT)
# GPIO.setup(,GPIO.OUT)
# GPIO.setup(,GPIO.OUT)
# GPIO.setup(,GPIO.OUT)
# GPIO.setup(,GPIO.OUT)
# GPIO.setup(,GPIO.OUT)
# GPIO.setup(,GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    client.subscribe("led1")
    client.subscribe("led2")
    client.subscribe("led3")
#     client.subscribe("led4")
#     client.subscribe("led5")
#     client.subscribe("led6")
#     client.subscribe("led7")
#     client.subscribe("led8")
#     client.subscribe("led9")
#     client.subscribe("led10")
#     client.subscribe("led11")
def on_message(client, userdata, msg):
    var=format(msg.payload.decode("utf-8"))
    if msg.topic=="led1":
        if var=="on":
            GPIO.output(4,GPIO.HIGH)
            print("led1 on")
        else:
            GPIO.output(4,GPIO.LOW)
            print("led1 off")
    if msg.topic=="led2":
        if var=="on":
            GPIO.output(26,GPIO.HIGH)
            print("led2 on")
        else:
            GPIO.output(26,GPIO.LOW)
            print("led2 off")
    if msg.topic=="led3":
        if var=="on":
            GPIO.output(27,GPIO.HIGH)
            print("led3 on")
        else:
            GPIO.output(27,GPIO.LOW)
            print("led3 off")
            '''
    if msg.topic=="led4":
        if var=="on":
            GPIO.output(,GPIO.HIGH)
        else:
            GPIO.output(,GPIO.LOW)
    if msg.topic=="led5":
        if var=="on":
            GPIO.output(,GPIO.HIGH)
        else:
            GPIO.output(,GPIO.LOW)
    if msg.topic=="led6":
        if var=="on":
            GPIO.output(,GPIO.HIGH)
        else:
            GPIO.output(,GPIO.LOW)
    if msg.topic=="led7":
        if var=="on":
            GPIO.output(,GPIO.HIGH)
        else:
            GPIO.output(,GPIO.LOW)
    if msg.topic=="led8":
        if var=="on":
            GPIO.output(,GPIO.HIGH)
        else:
            GPIO.output(,GPIO.LOW)
    if msg.topic=="led9":
        if var=="on":
            GPIO.output(,GPIO.HIGH)
        else:
            GPIO.output(,GPIO.LOW)
    if msg.topic=="led10":
        if var=="on":
            GPIO.output(,GPIO.HIGH)
        else:
            GPIO.output(,GPIO.LOW)
    if msg.topic=="led11":
        if var=="on":
            GPIO.output(,GPIO.HIGH)
        else:
            GPIO.output(,GPIO.LOW)
            '''
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("musach.tk", 1883)

client.loop_forever()