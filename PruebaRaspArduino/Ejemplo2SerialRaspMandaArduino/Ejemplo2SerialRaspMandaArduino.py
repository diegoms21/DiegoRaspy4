import serial
s = serial.Serial("/dev/ttyACM0",9600)
flag = True
while flag:
    a = input("digite una letra: ")
    if a == "fin":
        flag = False
    else:
        s.write(a.encode())#estamos enviando un string, con encode mandamos una cadena de bytes
s.close()