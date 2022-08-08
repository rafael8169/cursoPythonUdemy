print("Debido a una actaulizacion de Python 3.10")
print("Es la opcion de switch o switch case que en python se maneja con 'elif' a partir de la version 3.10")
print("La nueva herramienta se llama  'match' elegir una opcion entre varias y haga algo de acuerdo a una entrada")
print("Ejemplo este se haria con if antes de la version 3.10")

serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe este producto")

print("Ejemplo con match")
match serie:
  case "N-01":
    print("Samsung")
  case "N-02":
    print("Nokia")
  case "N-03":
    print("Motorola")
  case _:
    print("No existe este producto")

cliente = {'nombre' : 'Rafael',
               'edad': '40',
               'origen':'colombia'}
pelicula = {'titulo':'matrix',
             'ficha tecnica' : {'protagonista':'Keanu Reeves', 'director':'Lana Y Lili Wachovsky'}}
elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre':nombre,
              'edad':edad,
              'origen':origen}:
            print("Es un cliente")
            print(nombre,edad,origen)
        case {'titulo':titulo,
              'ficha tecnica':{'protagonista':protagonista,'director':director}}:
            print("E una pelicula existente")
            print(titulo,director)
        case _:
            print(f"No se que es esto '{elementos[2]}'")


