import socket
s = socket.socket()

s.connect(("192.168.1.6",2020))
print("conectado al servidor")
continuar = True
while continuar:
    dato = input("digite un dato a enviar: ")
    if dato == "z":
        continuar  = False
    else:
        s.send(dato.encode())
s.close()
print("fin de programa")