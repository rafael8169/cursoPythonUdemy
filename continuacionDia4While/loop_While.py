
pregunta = input("Quiere continuar con el programa? : escriba 'SI' o 'NO'")

while pregunta == 'SI':
    pregunta = input("Quiere continuar con el programa? : escriba 'SI' o 'NO'")
else:
    print("Gracias")

monedas = 10

while monedas > 0:
    print(f"Le quedan {monedas}")
    monedas -= 1
print(f"le quedan {monedas} MONEDAS")



print("USO DE PASS")
password = '123'
respuesta = input("Escriba la contraseña")
while password != respuesta:
    respuesta = input("Escriba la contraseña")
else:
    print("Respuesta correcta")
respuesta2 = 's'

while respuesta2 != 's':
    pass
print("pass")

nombre = input("Escriba su nombre completo con apellidos").title()

lista = nombre.split()
print(lista)

for i in lista:
    apellido = input("Escriba apellido para buscar coincidencia").title()
    if apellido == i:
        print(f"Su apellido {apellido} SI se encuentra en el nombre")
        break


