import tkinter
#from tkinter import *  -- para importar todo
class Numero:
    def __init__(self):
        self.contador = 0 #creo una clase para que el objeto que lo instancie sea global y lo use en todas las funciones       

def dismunuir():
    print("dismunuir")
    conta.contador = conta.contador - 1
    etiqueta.set(conta.contador)
    
def aumentar():
    print("aumentar")
    conta.contador = conta.contador + 1
    etiqueta.set(conta.contador) #con esto le asigno a la etiqueta el valor del contador del objeto conta

w = tkinter.Tk()
w.title("Demo")
etiqueta = tkinter.StringVar() #creamos una etiqueta que variará su valor
conta = Numero()
etiqueta.set("0") #lo seteamos en un nuevo valor

fm = tkinter.Frame(w)
fm.grid(row=0,column=0)

bt1 = tkinter.Button(fm, text = "Disminuir", command = dismunuir, height = 2, width = 20)
bt1.grid(row =1, column=0)
bt2 = tkinter.Button(fm, text = "Aumentar", command = aumentar, height = 2, width = 20)
bt2.grid(row =1, column=1)
lb = tkinter.Label(fm, textvariable = etiqueta, height=2) #si queremos una etiqueta que varie su valor colocamos textvariable|sino solo text="..."
lb.grid(row=2,column=0, columnspan=2) #columnspan es para que ocupe 2 columnas

w.mainloop()