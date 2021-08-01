'''RPY como Servidor'''
import socket
import RPi.GPIO as GPIO

'''GPIO'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)


'''SOCKET SERVER'''
s = socket.socket()
s.bind(("19.168.1.6",2020)) #ip de la raspberry
s.listen(10)

while True:
    (sc,addrc) = s.accept()
    print("cliente conectado: ", addrc)
    continuar = True
    while continuar:
        dato = sc.recv(64)
        if not dato: #si no hay datos se desconecta
            continuar = False
            print("cliente desconectado")
        else: #en caso si haya dato, lo pasa de bytes a string
            dato2 = dato.decode()
            if dato2 == "a":
                print("led encendido")
                GPIO.output(2,GPIO.HIGH)
            elif dato2 == "b":
                print("led apagado")
                GPIO.output(2,GPIO.LOW)
s.close()
print("fin de programa")