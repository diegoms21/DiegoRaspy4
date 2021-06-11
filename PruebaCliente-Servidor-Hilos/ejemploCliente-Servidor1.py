#el cliente se conecta, el servidor lee la ip y acaba el programa
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #utiliza ipb4 con af_inet, que utilice tcp con socket_stream
s.bind(("192.168.1.46",2019))#ip del servidor (raspberry) y en el puerto 2019
s.listen(5) #acepta 5 conecciones en simultaneo
print("esperando un cliente")
#esperamos al cliente a que se conecte en la linea de abajo
(sc,addrC) = s.accept() #cuando el cliente se conecte se crea el socket del cliente y la direccion ip del cliente
print("se conecto el cliente")
print("ip del cliente ", addrC)
sc.close()#cerrar el socket del cliente
s.close()#cerrar el socket del servidor
print("fin de programa")