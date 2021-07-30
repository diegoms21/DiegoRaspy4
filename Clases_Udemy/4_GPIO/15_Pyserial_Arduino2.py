import serial
s = serial.Serial("/dev/ttyACM0",9600)

continuar = True
while continuar:
    dato = input("digite una letra: ")
    if dato == "z":
        continuar = False
    else:
        s.write(dato.encode()) #se envian bytes por la funcion write, por eso usamos encode, convertimos el string a byte
s.close()
print("fin de programa")

#decode() para convertir cadena de bytes a string
#encode() para convertir cadena de string a bytes