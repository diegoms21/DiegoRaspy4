#diccionario tiene un parámetro y este tiene un valor
#puede haber un diccionario adentro de otro diccionario
dicc = {"nombre":"diego", "edad":24, "notas":{"fisica":14, "quimica":16, "matematica":19}}
print(type(dicc))
#agregar un elemento
dicc["licencia"] = True
dicc["Sexo"] = "Masculino"
for i in dicc:
    print(i) #imprime todos los parametros
    print(dicc[i]) #imprime todos los valores
    
#crear un conjunto de tuplas desde un diccionario
a = dicc.items()
for i in a:
    print(i) #imprime los parametros
    print(i[0]) #imprime los valores de los parametros que le coloque