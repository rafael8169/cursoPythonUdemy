print("desde,hasta,posiciones o intervalos")

lista = list(range(1, 5))
print(f"Lista inicial {lista}")

for i in range(len(lista)):
    print(i)
    lista.append(i)
print(f"lista modificada {lista}")

mi_lista = list(range(3,301,3))

print("sumar todos los cuadrados de los numeros del 1 al 15")

suma_cuadrados = 0

for i in range(1,16):
    j = i*i
    #print(j)
    suma_cuadrados = j + suma_cuadrados
print(suma_cuadrados)

