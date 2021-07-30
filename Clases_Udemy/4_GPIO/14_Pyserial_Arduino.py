#sudo apt-get install arduino
'''LIBERIA pyserial
import serial
s = serial.Serial(puerto,baudiaje) como "ACM0",9600

#Funciones
dato = s.read() #lee un byte
dato = s.read(n) #lee n bytes
dato = s.readline() #lee una cadena de texto
s.write(data) #envia la información
s.close() #cerramos el puerto serial
'''

import serial
s = serial.Serial("/dev/ttyACM0",9600)

try:
    while True:
        dato = s.readline()
        print(type(dato),dato.decode()) #envia una cadena de bytes, si quiero convertirlo a string
                                        #uso decode()
except:
    s.close()
    print("fin de programa")

#decode() para convertir cadena de bytes a string
#encode() para convertir cadena de string a bytes