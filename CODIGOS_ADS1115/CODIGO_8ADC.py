import time
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} | {4:>6} | {5:>6} |'.format(*range(6)))
print('-' * 55)

while True:
    values = [0]*6
    for i in range(6):
        values[i] = adc.read_adc(i, gain=GAIN)
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} | {4:>6} | {5:>6} |'.format(*values))
    time.sleep(0.5)