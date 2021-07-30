import Adafruit_DHT as dht
import lcddriver
import time

sensor = dht.DHT11
lcd = lcddriver.lcd()

h,t = dht.read_retry(sensor,4) #objeto sensor conectado al pin 4

try:
    while True: #t y h son float, para imprimirlos en el display los pasamos a string
    h,t = dht.read_retry(sensor,4) #lee el sensor
    lcd.lcd_display_string("T=" + str(t), 1) #temperatura en fila 1
    lcd.lcd_display_string("H=" + str(h), 2) #humedad en fila 2
    time.sleep(3)
    lcd.lcd_clear()
except: #salimos cn Ctrl+C
    print("fin de programa")