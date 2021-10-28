#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Un avión que viaja 800 Km/hr. Dispara un proyectil auto impulsado,
en el momento del disparo, el avión hace un giro de 90 grados y acelera a 20 mtrs/seg2.
El proyectil sigue su curso, acelerando a 10 mtrs./seg2.
Diseñe un pseudocódigo que escriba cada segundo, la distancia que separa al avión del proyectil,
hasta que estén a 10,000 mtrs. o más.
'''


tiempo = 0
velocidad_ovni = 20  # mt/s
velocidad_proyectil = 10  # mt/s

# distancia = velocidad * tiempo
desplazamiento_ovni = velocidad_ovni * tiempo
desplazamiento_proyectil = velocidad_proyectil * tiempo
distancia_total = desplazamiento_ovni + desplazamiento_proyectil

print('tiempo: {} distancia: {}'.format(tiempo, distancia_total))
while distancia_total <= 10000:
    tiempo = tiempo + 1

    desplazamiento_ovni = velocidad_ovni * tiempo
    desplazamiento_proyectil = velocidad_proyectil * tiempo
    distancia_total = desplazamiento_ovni + desplazamiento_proyectil

    print('tiempo: {} distancia: {}'.format(tiempo, distancia_total))
    print("-- desplazamiento_ovni: {} desplazamiento_proyectil: {}".format(desplazamiento_ovni, desplazamiento_proyectil))

    print()
print('fin')





