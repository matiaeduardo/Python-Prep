#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
f = 1
print(f)

#2) Imprimir el tipo de dato de la constante 8.5
c = 8.5
print(c)
#3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(f))
# 4) Crear una variable que contenga tu nombre
name = 'Matias'
# 5) Crear una variable que contenga un número complejo
complejo = 1 + 1j
# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(complejo))
# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi = 3.1416
# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
vTrue = True
sTrue = 'True'
'No, porque son distintos tipos de datos. Booleano y Str.'
# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(type(vTrue),type(sTrue))
# 10) Asignar a una variable, la suma de un número entero y otro decimal
enteroDecimal = 5 + 5.5
# 11) Realizar una operación de suma de números complejos
complejo2 = complejo + 7 + 7j
print(complejo2)
# 12) Realizar una operación de suma de un número real y otro complejo
complejo3 = complejo2 + 2
print(complejo3)
# 13) Realizar una operación de multiplicación
multiplicacion = 5*5
# 14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)
# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
div = 27/4
print(div)
# 16) De la división anterior solamente mostrar la parte entera
div2 = 27//4
print(div2)
# 17) De la división de 27 entre 4 mostrar solamente el resto
div3 = 27%4
print(div3)
# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
var18 = div2*4+div3
# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print('hola ' + 'persona')
# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
a = '2' == 2
print(a)
'Porque en str no es igual a int, por ende retorna un booleano.'
# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
a = int('2') == 2
print(a)
# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a=float('3,8')
a = float('3.8')
print(a)
'Porque se utiliza el sistema decimal americano.'
# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
var23 = 3
var23 -= 1
print(var23)
# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
var24 = 1<<2
'convierte el 1 en numero binario y realiza un despazamiento hacia la izquiera de dos bits. Es el sistema de numeracion de dos digitos (1, 0)'
print(var24)
# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
var25 = 2+'2'
'Daría error porque no se puedo sumar caracteres y un numero. No, porque si sumamos el "2"+"2" daria de resultado "22".'
# 26) Realizar una operación válida entre valores de tipo entero y string
print('Hola '*3)
