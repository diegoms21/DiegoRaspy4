#con ipconfig vemos la ip de la pc usando el cmd
import socket
import threading as th

'''Una vez que se conecta un cliente, imprime sus datos
y espera a recibir un mensaje, si el mensaje es vacío, sale
del while y desconecta al cliente, caso contrario lo imprime'''
def manejar(sc,addrc):
    print("cliente conectado: ", addrc)
    continuar = True
    while continuar:
        dato = sc.recv(64)
        if not dato:
            continuar = False
            print("cliente desconectado")
        else:
            print(dato)
    sc.close()

s = socket.socket()
s.bind(("19.168.1.6",2020))
s.listen(10)
print("iniciando servidor")

'''cuando llegue un cliente le generará un hilo y
esperará nuevamente a otro cliente'''
while True:
    (sc,addrc) = s.accept()
    hilo = th.Thread(target = manejar, args = (sc,addrc))
    hilo.start()
    
print("fin de programa")
s.close()