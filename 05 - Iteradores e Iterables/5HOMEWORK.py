# ## Iteradores e iterables
# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1
""" 
var1 = []
a = 15
while a >= 1:
    var1.append(-a)
    a -=1
print(var1) 
 """
# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?
""" i = 0
while i< len(var1):
    if var1[i]%2 == 0:
        print(var1[i])
    i += 1  """
# 3) Resolver el punto anterior sin utilizar un ciclo while
""" for i in var1:
    if i%2 == 0:
        print(i,end=' ')
         """
# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos
""" var4 = iter(var1)
print(next(var4))
print(next(var4))
print(next(var4))
 """
""" for i in var1[:3]:
    print(i) """
# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento
""" for i, c in enumerate(var1):
    print(i,c)
 """
# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: 
""" lista = [1,2,5,7,8,10,13,14,15,17,20]
for i in range(1,21):
    if (not(i in lista)):
        lista.insert((i-1),i)
print(lista) 
"""
# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>
""" 
num0 = 0
num1 = 1
lista = [num0,num1]
while len(lista) < 30:
    x = num0+num1
    lista.append(x) 
    num0 = num1
    num1 = x
print(lista) """
""" 
fibona = [0,1]
while (len(fibona)<30):
    fibona.append(fibona[-1]+fibona[-2])
print(fibona)
 """
# 8) Realizar la suma de todos elementos de la lista del punto anterior
""" 
fibona = [0, 1]
while (len(fibona) < 30):
    fibona.append(fibona[-1]+fibona[-2])
print(fibona)
 """
# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
""" for i in range(10,15):
    print(fibona[i]/fibona[i-1])
 """
# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
""" 
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for i,c in enumerate(cadena):
    if c == 'n':
        print(i)
         """
# 11) Crear un diccionario e imprimir sus claves utilizando un iterador
""" 
diccionario = {1:'a',2:'b',3:'c'}
for i in diccionario:
    print(i)
     """
# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 
""" cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
cadena = list(cadena)
for i in cadena:
    print(i,end='') """
"""     
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
cadena = list(cadena)
recorre = iter(cadena)
for i in range(0,len(cadena)):
    print(next(recorre),end='') """
    
# 13) Crear dos listas y unirlas en una tupla utilizando la función zip
""" 
= [1,2,3,4,5]
listaB= [6,7,8,9,0]
listaC = zip(listaA,listaB)
print(list(listaC))
 """
# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
""" lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100] """
""" lista = []
for i in lis:
    if i%7 == 0:
        lista.append(i)
print(lista) """
""" lista = [a for a in lis if i%7 == 0]
print(lista)
 """
# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
""" 
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
contador = 0
for i in lis:
    if type(i) == list:
        contador += len(i)
    else:
        contador += 1
print(contador)
 """
# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es
""" 
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
for i,c in enumerate(lis):
    if type(i) != list:
        lis[i] = [c]
print(lis) """