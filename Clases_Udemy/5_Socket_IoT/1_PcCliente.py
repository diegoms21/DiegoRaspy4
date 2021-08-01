import socket

s = socket.socket()
s.connect(("192.168.1.2",2020)) #conecta con la rpy

continuar = True
while continuar:
    dato = input("digite lo que desea enviar: ")
    id dato == "z":
        continuar = False
        print("coneccion finalizada")
    else:
        s.send(dato.encode()) #envia bytes, con encode lo convertimos de string

s.close()
print("fin de programa")