import serial
s = serial.Serial("/dev/ttyACM0",9600)

while True:
    a = s.readline()
    print(a)
s.close()

