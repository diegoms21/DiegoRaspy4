import RPi.GPIO as GPIO
import tkinter
import time

'''FUNCIONES'''
def cambio(valor):
    print(type(valor),valor)
    etiqueta.set(valor)
    dc = (angulo + 45)/18 #en el txt del curso está la explicacion
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.2)

'''GPIO'''
GPIO.setmode(BPIO.BCM)
GPIO.setup(2,GPIO.OUT)
pwm = GPIO.PWM(2,50) #50Hz servomotor
pwm.start(2.5) #inicia con DC=0 y angulo 

'''TKINTER INICIAL'''
w = tkinter.Tk()
fm = tkinter.Frame(w)
fm.grid(row=0, column=0)

'''ETIQUETA'''
etiqueta = tkinter.StringVar()
etiqueta.set(0)

'''SLIDE BAR'''
sl = tkinter.Scale(fm, from_=0, to = 180, orient = tkinter.HORIZONTAL, command = cambio, length = 200)
sl.grid(row=1, column=0)

'''LABEL'''
lb = tkinter.Label(fm,textvariable =  etiqueta, width = 20, height = 2)
lb.grid(row=2, column=0)

w.mainloop()
pwm.stop()
GPIO.cleanup()
print("Fin de programa")