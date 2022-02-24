#1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es
""" 
def primo(lista):
    esPrimo = True
    for i in lista:
        if lista%i == 0:
            esPrimo = False
            break
    return esPrimo
 """
#2) Usando la función del punto 1, realizando otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista
""" 
def verifica_primo(nro):
    es_primo = True
    for i in range(2, nro):
        if nro % i == 0:
            es_primo = False
            break
    return es_primo

def extrae_primos_de_lista(lista):
    lista_primos = []
    for elemento in lista:
        if verifica_primo(elemento): # == a poner true(int)??
            lista_primos.append(elemento)
    return lista_primos

print(extrae_primos_de_lista([1, 2, 3,4 , 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))

 """


#3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuantas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

""" def repetidor(lista):
    resultado = {}
    for i in lista:
        if i in resultado:
            resultado[i] += 1
        else:
            resultado[i] = 1
    mNum = 0
    mFreq = 0
    for num, freq in resultado.items():
        if freq > mFreq:
            mNum = num
            mFreq = freq
    return f'El numero con mas repeticiones es el {mNum} y aparece {mFreq} veces'
lista = [1, 1, 5, 6, 8, 10, 22, 5, 6, 4, 11, 9, 5]
print(repetidor(lista))
 """

#4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.


def repetidor(lista):
    resultado = {}
    for i in lista:
        if i in resultado:
            resultado[i] += 1
        else:
            resultado[i] = 1
    mNum = 0
    mFreq = 0
    for num, freq in resultado.items():
        if freq > mFreq:
            mNum = num
            mFreq = freq
    
    
    return f'El numero con mas repeticiones es el {mNum} y aparece {mFreq} veces'


lista = [1, 1, 5, 6, 8, 10, 22, 5, 6, 4, 11, 9, 5]
print(repetidor(lista))











# Crear una función que convierta entre grados Celsius, Farenheit y Kelvin
# Fórmula 1: (°C × 9/5) + 32 = °F
# Fórmula 2: °C + 273.15 = °K
# Debe recibir 3 parámetros: el valor, la medida de origen y la medida de destino

# Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer una impresión para cada combinación de los mismos:

# Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar un parámetro un número no entero o negativo
