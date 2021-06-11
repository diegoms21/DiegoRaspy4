import serial
s = serial.Serial("/dev/ttyACM0",9600)

while True:
    a = s.readline()
    b = a.decode()#quitamos los bytes y lo convertimos a string
    c = b.split(",").rstrip("\n")#separamos por la coma y lo volvemos un arreglo [temperatura,humedad]
    #con rstrip eliminamos el espacio producido por el salto de linea
    print("T=",c[0],",H=",c[1])
s.close()