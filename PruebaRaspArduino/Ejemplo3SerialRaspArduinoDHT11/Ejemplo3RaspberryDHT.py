import Adafruit_DHT as dht
import time
sensor = dht.DHT11 #dht.DHT22
while True:
    humedad, temperatura = dht.read_retry(sensor,4) #pin4 en BCM, o GPIO4
    print("T=", temperatura, "H=",humedad)
    time.sleep(0.5)    
print("Fin de programa")