## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
""" var1= 5
if var1>=0:
    print(f'{var1} Es mayor a cero')
else:
    print(f'{var1} Es menor a cero') """
#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
""" var2 = 2
variable2 = 2
if type(var2) == type(variable2):
    print(f'"{var2}" y "{variable2}" son el mismo tipo de dato: ({type(var2)}).')
else:
    print(f'No son el mismo tipo de datos.') """
#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
""" for i in range(1,21):
    if i%2 == 0:
        print(f'{i} Es PAR.')
    else:
        print(f'{i} Es IMPAR.') """
#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
""" for i in range(0,6):
    print(f'{i}³ = {i**3}') """
#5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
""" var5 = 5
for i in range(var5):
    pass """
#6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
""" var6= 5
if var6 > 0:
    fac = var6
    while var6 > 2:
        var6 = var6 - 1
        fac = fac * var6
    print(f'El factorial es {fac}')
else:
    ('No es mayor a cero') """
#7) Crear un ciclo for dentro de un ciclo while
""" var7 = 10
while var7>0:
    for i in range(var7):
        print('*',end='')
    print('*')
    var7 -=1 """
#8) Crear un ciclo while dentro de un ciclo for
""" var8 = 1
for i in range(10):
    while var8<11:
        print(var8, end=' ')
        var8 +=1 """
#9) Imprimir los números primos existentes entre 0 y 30
""" for i in range(0,31):
    contador = 0
    for j in range(2,i):
        if i%j == 0:
            contador +=1
    if contador == 0:
        print(i)  """   
#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
""" n=0
primo =True
while(n<30):
    for i in range(2,n):
        if n%i == 0:
            primo = False
            break
    if primo:
        print(n)
    else:
        primo = True
    n +=1 """
#11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
""" min=99
max=300
while min<=max:
    min += 1
    if min%12 != 0:
        continue
    print(min) """
#14) Utilizar la función ** input() ** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
""" while True:
    print('"0" para salir')
    numero = int(input('Ingrese numero: '))
    if numero>1:
        for i in range(2,numero):
            if(numero%i==0):
                print(f'{numero} No es primo\n')
                break
            else:
                print(f'{numero} Es Primo\n')
                break
    elif numero == 0:
        print('Buenas noches :)\n')
        break
    else:
        print('\nNo es mayor a uno, volver a ingresar.')
         """
#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
""" min = 100
while min<300:
    if min%6 == 0:
        print(min)
        break
    min +=1
 """