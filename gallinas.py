#!/usr/bin/env python
# -*- coding: utf-8 -*-


# mismo ejercicio con un while
cantidad_de_gallinas = 0
contador_para_el_promedio = 0
condicion = ''
while condicion != 0:
    condicion = input("""
        Menu de ejecicio
        1) Ingresar Gallina
        2) Calcular promedio que llevamos 
        
        0) salir

        seleccione su opcion
    """)

    if condicion == 1:
        cantidad_de_gallinas = cantidad_de_gallinas + 1
        print("=== Ingrese datos de la gallina Numero: {} ===".format(cantidad_de_gallinas))

        peso = int(input("ingrese peso de gallina: "))
        altura = int(input("ingrese altura de gallina: "))
        huevos = int(input("ingrese huevos de gallina: "))

        calidad_gallina = peso * altura / huevos
        print('calidad de esta gallina es: {}'.format(calidad_gallina))

        contador_para_el_promedio = contador_para_el_promedio + calidad_gallina

    elif condicion == 2:
        promedio = float(contador_para_el_promedio) / float(cantidad_de_gallinas)
        print("llevamos {} gallinas ingresadas hasta el momento".format(cantidad_de_gallinas))
        print('promeedio que llavamos: {}'.format(promedio))

promedio = float(contador_para_el_promedio) / float(cantidad_de_gallinas)
print("ingresamos {} gallinas".format(cantidad_de_gallinas))
print('venta por kilo de huevo: {}'.format(promedio))
print ('FIN!')

'''
    # x solicitamos al usuario los datos
    # x hago la operacion axb/c
    # x sumo en contador_para_el_promedio
    # pregunto hasta que el usuario se aburra


# calculo el promedio
# imprimo el promedio

'''








contador = 0
while True:
    condicion = input("""
        Bienvenido a ZP
        1) ordenar 
        2) servicio
        3) festas
        0) salir
        
        seleccione su opcion
    """)
    contador = contador + 1
    if condicion == 0:
        break
    if condicion == 1:
        print('pide una pizza')
    if condicion == 2:
        print('no hay nadie disponible, deja un mensaje')
    if condicion == 3:
        print('invitame')

print('se ejecuto {} veces '.format(contador))
print('se acabo chao! ')

"""

1. En una granja se requiere saber alguna información para determinar el precio de venta por cada kilo de huevo.
precio se determina a traves del promedio de calidad de las N gallinas que hay en la granja.
La calidad de cada gallina se obtiene según la formula:
calidad = (peso de la gallina * altura de la gallina)/Numero de huevos que pone;

"""


numero_de_gallinas = int(input("ingrese el numero de gallinas: "))
print('el numerno de gallinas es: {}'.format(numero_de_gallinas))
contador_para_el_promedio = 0
for i in range(numero_de_gallinas):

    print("=== Ingrese datos de la gallina Numero: {} ===".format(i))

    peso = int(input("ingrese peso de gallina: "))
    altura = int(input("ingrese altura de gallina: "))
    huevos = int(input("ingrese huevos de gallina: "))

    calidad_gallina = peso * altura / huevos
    print('calidad de esta gallina es: {}'.format(calidad_gallina))

    contador_para_el_promedio = contador_para_el_promedio + calidad_gallina

promedio = float(contador_para_el_promedio) / float(numero_de_gallinas)

print('venta por kilo de huevo: {}'.format(promedio))