import tkinter
import time
import threading as th

def aumentar():
    contador = 0
    while True:
        time.sleep(1)
        contador = contador + 1
        etiqueta2.set(contador)

def cambio(valor):
    etiqueta1.set(valor)

w = tkinter.Tk()

#etiqueta1
etiqueta1 = tkinter.StringVar()
etiqueta1.set(0)

#etiqueta2
etiqueta2 = tkinter.StringVar()
etiqueta2.set(0)

fm = tkinter.Frame(w)
fm.grid(row = 0,column = 0)

#definimos el slider
sl = tkinter.Scale(fm, from_=0, to=20, orient = tkinter.HORIZONTAL,length = 400,command=cambio)
sl.grid (row = 1, column = 0) #se ubicará en la fila 1 columna 0

#definimos el label1
lb1 = tkinter.Label(fm, textvariable = etiqueta1, height = 2)
lb1.grid(row = 2, column = 0)

#definimos el label2
lb1 = tkinter.Label(fm, textvariable = etiqueta2, height = 2)
lb1.grid(row = 3, column = 0)

#colocamos el hilo
hilo = th.Thread(target = aumentar)
hilo.start()

w.mainloop()

#creamos un slidebar que refleja su cambio en una caja de texto "label1" y luego colocamos otro texto
#"label2" que lo corremos en paralelo contando los segundos, usando hilos
