from random import shuffle

#Crear la lista con los datos
palitos = ['-', '--','---','----']

#crear funcion para mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#aqui comprobamos
#print(mezclar(palitos))

#crear funcion probar suerte sin ningun parametro

def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input("Ingrese un valor entre 1 y 4 : ")

    return int(intento)

#llamar funcion para comprobar intento
#var_intento = probar_suerte()
#print(var_intento)


#Comprobar intento
def revisar_resultado(lista,intento):
    if lista[intento - 1] == '-':
        #print(lista[intento-1])
        print("Graves le toco bañarse")
    else:
        print("Se salvo hermano")

    print(f"Sacaste {lista[intento - 1]}")

#llamada a las funciones

mezcla = mezclar(palitos)

pedir_numero = probar_suerte()

comprobar_resultado = revisar_resultado(mezcla,pedir_numero)