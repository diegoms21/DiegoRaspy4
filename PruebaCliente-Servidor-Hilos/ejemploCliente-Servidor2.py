#el cliente se conecta, el servidor lee la ip y acaba el programa
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.1.46",2019))
s.listen(5) 
(sc,addrC) = s.accept()
#se conecta el cliente
print("Ip del cliente ", addrC)
while True:
    mensaje = sc.recv(64) #se le da 64bytes, para TCP
    print("Mensaje: ", mensaje)
    men="Mensaje Recibido"
    sc.send(men.encode())
print("Fin de programa")
sc.close()#cerrar el socket del cliente
s.close()#cerrar el socket del servidor

