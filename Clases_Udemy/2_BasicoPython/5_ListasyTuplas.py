#la tupla es similar a una lista pero no se pueden modificar los elementos
#los elementos pueden ser diferentes
#lista y tuplas se encuentran ordenadas de izquierda a derecha desde 0, 1 , 2 , etc
# y se encuentran ordenadas de derecha a izquierda desde -1 , -2, -3, ...
lista1 = [3 , 2 , "hola",[10,"prueba"], (5,2,1),10]
lista2 = [1 , 5, 2 , 4]
tupla = (5 ,10 , "prueba", 5)

print (type(lista1),type(tupla))
print (max(lista2)) # min
lista2[-1] = lista2[0] + lista2[1] #esto no se puede hacer en una tupla, sus valores no cambian
a = list(tupla) #genero una lista basado en una tupla
print(lista2)
lista2.sort() #sirve para ordenar la lista de menor a mayor
lista2.sort(reverse=True) #imprime de mayor a menor
print(lista2)

#una lista puede tener listas adentro o tuplas adentro
print(lista1[3][1]) #del elemento 3 imprimo el primer elemento
print(lista1[4][-1])

#METODOS EN LISTAS

#ver el tamaño de la lista LEN
long = len(lista1)
print(long)

#añadir valores a la lista APPEND, si agrego una lista lo agerga como tal
lista1.append(10)
lista1.append([1,2])
print(lista1)

#agrega los elementos de una lista en otra lista EXTEND
lista1.extend([1,2])
print(lista1)

#remueve elemento que se le pase como parametro REMOVE
lista1.remove(1)
print(lista1)

#devuelve el indice del elemento mandado INDEX
indice = lista1.index("hola")
print(indice)

#invierte los elementos de una lista REVERSE
lista1.reverse()
print(lista1)