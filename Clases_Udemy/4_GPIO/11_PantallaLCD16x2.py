#Hay varias modificaciones que hacerle a la libería antes de usar este código
#Revisar el video del curso udemy

import lcddriver
import time

lcd = lcddriver.lcd()

'''HACE QUE EL MENSAJE AVANCE'''
texto = ""
maximo = 12
while maximo > 0:
    lcd.lcd_display_string(texto+"Hola",2)
    time.sleep(1)
    texto = texto + " "
    lcd.lcd_clear()
    maximo = maximo - 1
print("fin de programa")


''' CODIGO PARA HACER QUE PARPADE EL MENSAJE HOLA
try:
    while True: #Para que el mensaje parpadee
        lcd.lcd_display_string("hola",1) #mensaje hola en la fila 1
        time.sleep(1)
        lcd.lcd_clear()
        time.sleep(1)
except:
    print("fin de programa")'''
