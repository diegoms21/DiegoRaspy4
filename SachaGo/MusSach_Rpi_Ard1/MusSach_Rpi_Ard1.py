import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import serial

def on_connect(client, userdata, flags, rc):
    client.subscribe("led1")
    client.subscribe("led2")
    client.subscribe("led3")
    client.subscribe("led4")
    client.subscribe("led5")
    client.subscribe("led6")
    client.subscribe("led7")
    client.subscribe("led8")
    client.subscribe("led9")
    client.subscribe("led10")
#    client.subscribe("led11")
'''def consulta_topic(var,msj1,msj2,msj3):
    if var == "on":
        print(msj1 + " on")
        s.write(msj2.encode())
    else:
        print(msj1 + " off")
        s.write(msj3.encode())'''

def on_message(client, userdata, msg):
    s = serial.Serial("/dev/ttyACM1",9600)
    var=format(msg.payload.decode("utf-8"))

    if msg.topic=="led1":
        if var=="on":
            enviar = "led1 on"
            msj_ard='a'
            #print(type(msj_ard))
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
        else:
            enviar = "led1 off"
            msj_ard='b'
            print(enviar)
            s.write(msj_ard.encode())
    
    if msg.topic=="led2":
        if var=="on":
            enviar = "led2 on"
            msj_ard='c'
            print(enviar)
            s.write(msj_ard.encode())
        else:
            enviar = "led2 off"
            msj_ard='d'
            print(enviar)
            s.write(msj_ard.encode())
    if msg.topic=="led3":
        if var=="on":
            enviar = "led3 on"
            msj_ard='e'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
        else:
            enviar = "led3 off"
            msj_ard='f'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
    
    if msg.topic=="led4":
        if var=="on":
            enviar = "led4 on"
            msj_ard='g'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
            
        else:
            enviar = "led4 off"
            msj_ard='h'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
            
    if msg.topic=="led5":
        if var=="on":
            enviar = "led5 on"
            msj_ard='i'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
            
        else:
            enviar = "led5 off"
            msj_ard='j'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
           
    if msg.topic=="led6":
        if var=="on":
            enviar = "led6 on"
            msj_ard='k'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
            
        else:
            enviar = "led6 off"
            msj_ard='l'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
            
    if msg.topic=="led7":
        if var=="on":
            enviar = "led7 on"
            msj_ard='m'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
            
        else:
            enviar = "led7 off"
            msj_ard='n'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
           
    if msg.topic=="led8":
        if var=="on":
            enviar = "led8 on"
            msj_ard='o'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
        else:
            enviar = "led8 off"
            msj_ard='p'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
            
    if msg.topic=="led9":
        if var=="on":
            enviar = "led9 on"
            msj_ard='q'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
            
        else:
            enviar = "led9 off"
            msj_ard='r'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
            
    if msg.topic=="led10":
        if var=="on":
            enviar = "led10 on"
            msj_ard='s'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
            
        else:
            enviar = "led10 off"
            msj_ard='t'
            print(enviar)
            print(msj_ard)
            s.write(msj_ard.encode())
    '''       
    if msg.topic=="led11":
        if var=="on":
            GPIO.output(,GPIO.HIGH)
        else:
            GPIO.output(,GPIO.LOW)
            '''
    s.close()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("musach.tk", 1883)

client.loop_forever()