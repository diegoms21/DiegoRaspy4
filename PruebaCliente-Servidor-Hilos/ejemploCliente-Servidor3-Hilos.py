#el cliente se conecta, el servidor lee la ip y acaba el programa
import socket
import threading as th

def funcion(sc):
    while True:
        mensaje = sc.recv(64) #se le da 64bytes, para TCP
        print("Mensaje: ", mensaje)
        men="Mensaje Recibido"
        sc.send(men.encode())
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.1.46",2019))
s.listen(5)
while True:
    (sc,addrC) = s.accept()
    print("Ip del cliente ", addrC)
    hilo = th.Thread(target=funcion, args=(sc,))
    hilo.start()
    
print("Fin de programa")
sc.close()
s.close()


