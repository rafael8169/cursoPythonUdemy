nombres = ['Ana','Pedro','Hugo']
numeros = [10,20,30,40,50,60]
print("solo toma los valores con el tamaño de la lista mas corta el resto los ignora")
combinados = list(zip(nombres,numeros))

print(type(combinados))
print(combinados)

print("le voy a añadir otra list osea 3 listas juntas")
paises = ['Mexico','Colombia','Chile']
combinado2 = list(zip(nombres,numeros,paises))
print(combinado2)

for nom, num, pai in combinado2:
    print(f"{nom} tiene {num} años y vive en {pai}")

enum = dict(enumerate(combinado2))
print(enum)

print(enum.values())
print(enum.keys())
print(enum.items())
print(enum.get(0))
print(enum.__getitem__(0))


valores = enum.get(0)
print(f"Los valores almacenados en la clave '{enum.__contains__(0)}' son {valores}")
print(f"Los valores almacenados en la clave '{enum}' son {valores}")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for j, i in zip(capitales,paises):
    print(f"La capital de {i} es {j}")

marcas = ['Audi', 'BMW','Mercedez']
productos = ['Carros','Camiones', 'Buses']
mi_zip = list(zip(marcas,productos))
print(mi_zip)


espa = ['uno','dos', 'tres', 'cuatro', 'cinco']
portu = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one','two', 'three','four','five']
numeros = list(zip(espa,portu,ingles))

print(numeros)