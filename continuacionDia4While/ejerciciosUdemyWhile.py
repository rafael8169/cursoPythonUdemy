print("Escribir numeros del 10 al 0 uno a uno a la vez")

numeros = 10

while numeros >= 0:
    print(numeros)
    numeros-=1

print("Escribir numeros que reste del 50 al 0 uno a uno a la vez y solo muestre los numeros divisibles por 5")

numero = 50

while numero >= 0:
    print(numero)
    if numero%5 == 0:
        print(f"Este numero {numero} si es divisible por '5'")
    numero-=1

print("imprimir cada elemento de la lista e interrumpir el flujo cuando encuentre un nuemro negativo")
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for i in lista_numeros:
    if i < 0:
        break
    else:
        print(i)

