valor_anterior = 0
valor_actual = 1
print(valor_anterior)
print(valor_actual)
contador = 0
while True:
     auxiliar = valor_actual
     valor_actual = valor_anterior + valor_actual
     print(contador, valor_actual)
     valor_anterior = auxiliar
     contador = contador + 1
     if contador > 200:
         print('fin')
         break

     # if valor_actual > 1000:
     #     print('fin')
     #     break