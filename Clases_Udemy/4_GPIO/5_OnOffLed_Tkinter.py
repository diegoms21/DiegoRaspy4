import tkinter
import RPi.GPIO as GPIO

def apagar():
    print("apagar")
    GPIO.output(2,GPIO.LOW)
    etiqueta.set("Apagado")
def encender():
    print("encender")
    GPIO.output(2,GPIO.HIGH)
    etiqueta.set("Encendido")
    
'''GPIO'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.LOW)
    
'''PARAMETROS TKINTER'''
w = tkinter.Tk()
fm = tkinter.Frame(w)
fm.grid (row = 0, column = 0)

'''definir la etiqueta de estado que ira en el label'''
etiqueta = tkinter.StringVar()
etiqueta.set("Apagado")

'''PRIMER BOTON PARA APAGAR'''
b1 = tkinter.Button(fm, text = "Apagar", command = apagar, height = 2, width = 20)
b1.grid(row=1, column=0)

'''SEGUNDO BOTON PARA ENCENDER'''
b2 = tkinter.Button(fm, text = "Encender", command = encender, height = 2, width = 20)
b2.grid(row=1, column=1)

'''TEXTO O LABEL'''
lb = tkinter.Label(fm, textvariable = etiqueta, height = 2)
lb.grid(row=2,column=0,columnspan=2)

w.mainloop()