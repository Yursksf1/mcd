'''
if: condicional cuando se cumple
else: condicional cuando no se cumple

for: ciclos, finitos, definidos (donde yo se cuando se acaba)
while ciclos, medio infinitos, ( y no se cuando va a acabar)


for i in range(n):
   #do something

contador = 0
while contador < n:
    contador = contador +1
    #do something




while condicion:
    #do something


for i in ???:
    #do something

while True:
    if condicion >10:
        break
    # do something
    condicion = condicion +1


while True:
    condicion = input("seleccione 0 para salir")

    if condicion == 0:
        break
    # do something


'''

"""
tenemos un dia libre, vamos a definir que hacer a partir del dinero que tengamos disponible
"""

# mac va a ahorra 10.000 cada mes:
ahorros_de_mac = 0
meses = int(input("Igrese el Numero de meses para ahorrar: "))
for i in range(meses):
    ahorros_de_mac = ahorros_de_mac + 10000
print('mac alcanzo a ahorrar: ', ahorros_de_mac)

ahorros_de_yurs = 0
while ahorros_de_yurs < 70000:
    monto_a_ahorrar = int(input("Igrese lo que tengo en los bolsillos: "))
    ahorros_de_yurs = ahorros_de_yurs + monto_a_ahorrar

print('yurs alcanzo a ahorrar: ', ahorros_de_yurs)

gasto_de_yurs = 40000

ahorros_de_yurs = ahorros_de_yurs - gasto_de_yurs

dinero = ahorros_de_mac + ahorros_de_yurs

if dinero > 100000:
    print("tenemos: {}. vamos a la playa!".format(dinero))

elif dinero > 50000:
    print("tenemos: {}. vamos a cenar".format(dinero))
    print("""
        Menu:
        1) Pizza
        2) sushi
    """)
    opcion = int(input("Igrese el Numero de lo que desea comer: "))

    if opcion == 1:
        print ('drisfruta la pizza')
    else:
        print ('me encanta el sushi!')

else:
    print('tenemos: {}. vamos a cine!'.format(dinero))

print('hoy sera un gran dia!')









condicion = False
condicion_2 = True

if condicion:
    print 1
else:
    if condicion_2:
        print 3
    print 2



if condicion:
    print 1
elif condicion_2:
    print 3
else:
    print 2

