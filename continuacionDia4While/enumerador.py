lista = ['a', 'b', 'c', 1, 2, 3]

for i in enumerate(lista):
    print(i)

print("otro ejemplo")

for indice, item in enumerate(lista):
    print(indice, item)

print("una lista con un rango especifico")

for indice, item in enumerate(range(20, 29)):
    print(indice, item)

print("Lista con tuples dentro")

mi_lista = list(enumerate(lista))
print(type(mi_lista))
print(mi_lista)
print("tupla con tuplas dentro")
mi_tupla = tuple(enumerate(lista))
print(type(mi_tupla))
print(mi_tupla)
print(mi_tupla[1][1],mi_tupla[2][0])
print("diccionario con tuplas dentro")
mi_diccionario = dict(enumerate(lista))
print(type(mi_diccionario))
print(mi_diccionario)

print("consultar un valor diccionario")

print(mi_diccionario[4])
print(mi_diccionario.items())
print(mi_diccionario.keys())
print(mi_diccionario.keys().__contains__('a'))
print(mi_diccionario.keys().__contains__(1))
print(mi_diccionario.values())
# esto no me sirvio print(mi_diccionario.values().__contains__('b'))

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

palabra = "Python"
mia_lista = list(enumerate(palabra))
print(type(mi_lista))
print(mia_lista)

print("Imprimir solo los indices de aquellos nombres de la lista que comiencen por M")
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]


for indice, items in enumerate(lista_nombres):
    if items[0] == 'M':
        print(indice)

print("aqui imprimi indice y elemento")
for indice, item in enumerate(lista_nombres):
    if item[0] == 'M':
        print(indice,item)
