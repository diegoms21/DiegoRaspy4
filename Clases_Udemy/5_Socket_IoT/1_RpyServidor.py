'''RPY SERVIDOR / PC CLIENTE'''
'''el programa se detendrá en el accept porque esperará
que alguien se conecte, y al conectarse alguien esperará
en el rev que espera datos que le envie el cliente'''
import socket

s = socket.socket()
s.bind(("192.168.1.2",2020)) #colocamos la ip de la raspberry
s.listen(10) #escucha 10 conecciones como max en simultaneo
print("Esperando conecciones...")

#esperar a que acepte conecciones
(sc,addrc) = s.accept()
print("Cliente conectado con direccion: ",addrc)
continuar = True

while continuar:
    dato = sc.recv(64) #le asignamos 64 bytes para recibir
    if not dato: #si no hay datos o es nulo acaba el programa
        continuar = False
        print("cliente desconectado")
    else:
        print(dato)
    
sc.close() #cerrar siempre el cliente
s.close() #cerrar el servidor
print("fin de programa")