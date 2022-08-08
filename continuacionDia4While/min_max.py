lista = [11,22,1,55,100,0.1,-100,100.005]
print(f"el numero menor es {min(lista)} y el numero mayor es {max(lista)}")

nombres = ['Ardillita', 'Diana','Patricia']
print(f"el numero menor es {min(nombres)} y el numero mayor es {max(nombres)}")
nombres1 = ['ardillita', 'DIaNa','patriCia']
print(f"el numero menor es {min(nombres1)} y el numero mayor es {max(nombres1)}")
print(f"el numero menor es {min(nombres1).lower()} y el numero mayor es {max(nombres1).lower()}")
nombres1.sort()
print(nombres1)

print("Se puede con diccionarios y traer el valor minimo o maximo")

dic = {'C1':11, 'C2':12, 'C3':0.05}
print(min(dic),max(dic))
print(min(dic.values()),max(dic.values()))

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
print(lista_numeros)
valor_maximo = max(lista_numeros)
print(valor_maximo)

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros)-min(lista_numeros)
print(rango)

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print(edad_minima)
print(ultimo_nombre)