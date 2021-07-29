import RPi.GPIO as GPIO
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.1.46",2019))
s.listen(5)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.LOW)
bandera=True
(sc,addr) = s.accept()
print("Cliente conectado: ", addr)
while (bandera==True):
    mensaje = sc.recv(64)
    men = str(mensaje)[2:3] #hay que convertirlo a string porque por el protocolo se envian bytes
    #como envia b'a', ponemos [2:3] para agarrar solo el a de todo el string
    print("mensaje: ", men)
    if men == "a":
        GPIO.output(2,GPIO.HIGH)
    elif men == "b":
        GPIO.output(2,GPIO.LOW)
    elif men == "z":
        bandera = False
    else:
        print("Digite una letra correcta, a,b o z")
s.close()
sc.close()
print("Programa finalizado")

#correr con el programa del cliente en el temp.py linea 379 de spyder