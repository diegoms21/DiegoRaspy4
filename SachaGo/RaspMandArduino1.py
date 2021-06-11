import serial
s = serial.Serial("/dev/ttyACM1",9600)
flag = True
while flag:
    a = input("digite una letra: ")
    if a == "fin":
        flag = False
    else:
        print(type(a))
        s.write(a.encode())#estamos enviando un string, con encode mandamos una cadena de bytes
s.close()
