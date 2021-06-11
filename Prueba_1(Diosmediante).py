import pyfirmata
import time
board = pyfirmata.Arduino('/dev/ttyACM0')
pin12= board.get_pin('d:12:o')
while True:
    time.sleep(1)
    print("on")
    pin12.write(1)
    time.sleep(1)
    print("off")
    pin12.write(0)