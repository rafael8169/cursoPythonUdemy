# ejemplo como se trabajan las listas con for habitualmente
palabra = 'Python en muy bueno para aprender a programar'
lista = []

for i in palabra:
    lista.append(i)
print(lista)

lista.reverse()
print(lista)

print("Ahora utilizamos compresion de listas")

lista = [letra for letra in palabra]

print(lista)

print("Con numeros")
lista = [num for num in range(0, 20, 2)]
print(lista)

print("Con numeros")
lista = [num / 2 for num in range(0, 20, 2)]
print(lista)

print("Puedo poner dentro condicionales")
print("Con numeros")
lista = [num for num in range(0, 21, 2) if num * 2 > 12]
print(lista)

print("Si le pongo en la condicional el 'else' hay que escribirlo diferente")
print("'variable' if 'variable' operador logico 'valor'  else 'accion' for 'variable' in 'variable Lista,String/rango/etc'")

lista = [num if num *2 > 10 else 'No es mayor a 10' for num in range(0,21,2) ]
print(lista)

print("OJO si escribo el print en el else me arroja none y un comportamiento extraño")
lista = [num if num *2 > 10 else print("No es mayor a 10") for num in range(0,21,2) ]
print(lista)

print("Ejercicio transformar pies a metros de una lsita pies y ponerlo en lista metros")

pies = [10, 20, 30, 40, 50, 300, 1000]
metros = [n *3.281 for n in pies]
print(metros)

print("Crear lista valores_cuadrado formada por los numeros de la lista valores, elevados al cuadrado")

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n**2 for n in valores]
print(valores_cuadrado)

print("Crear lista valores_pares formada por los numeros de la lista valores, que sean pares")
valores_pares = [n for n in valores if (n%2 == 0)]
print(valores_pares)

print("Pasar farenheit a celsius, C= (F -32)*(5/9)")
temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [((f-32)*(5/9)) for f in temperatura_fahrenheit]
print(grados_celsius)
