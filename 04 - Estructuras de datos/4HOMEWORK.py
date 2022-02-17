# ## Estructuras de Datos
# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
""" city = ['Moscu','Buenos Aires','Sidney','Granada','Roma'] """
""" print(city) """
# 2) Imprimir por pantalla el segundo elemento de la lista
""" city = ['Moscu', 'Buenos Aires', 'Sidney', 'Granada', 'Roma','Texas']
print(city[1]) """
# 3) Imprimir por pantalla del segundo al cuarto elemento
""" print(city[1:5]) """
# 4) Visualizar el tipo de dato de la lista
""" print(type(city)) """
# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
""" print(city[2:]) """
# 6) Visualizar los primeros 4 elementos de la lista
""" print(city[:4]) """
# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
""" city.append('Porto')
city.append('Roma')
print(city) """
# 8) Agregar otra ciudad, pero en la cuarta posición
""" city.insert(4,'Tokio')
print(city) """
# 9) Concatenar otra lista a la ya creada
""" newList = ['Berlin','Ciud.Mexico','Quito']
city.extend(newList)
print(city) """
# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
""" print(city.index('Roma')) """
'Marca el primer dato'
# 11) ¿Qué pasa si se busca un elemento que no existe?
""" print(city.index('asdsda')) """
'Marca error, no está en la lista'
# 12) Eliminar un elemento de la lista
""" city.remove('Roma')
print(city) """
# 13) ¿Qué pasa si el elemento a eliminar no existe?
'Marca error'
# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
""" var14 = city[-1]
print(var14) """
""" ultimo = city.pop()
print(ultimo) """
# 15) Mostrar la lista multiplicada por 4
""" print(city * 4) """
# 16) Crear una tupla que contenga los números enteros del 1 al 20
""" var16 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20) """
# 17) Imprimir desde el índice 10 al 15 de la tupla
""" print(var16[10:16]) """
# 18) Evaluar si los números 20 y 30 están dentro de la tupla
""" print(20 in var16)
print(30 in var16) """
# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
""" if not('Paris' in city):
    city.append('Paris')
    print(city,'Se agregó "Paris".')
else:
    print('Paris ya existia xd') """
# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
""" print(city.count('Paris'))
print(var16.count(5)) """
# 21) Convertir la tupla en una lista
""" var16 = list(var16)
print(type(var16)) """
# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
""" v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20 = var16
print(v1,v2,v3) """
# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
""" var23 = {'ciudad':city,'pais':('peru','rumania','rusia','jamaica','portugal','chad'),'continente':('america','asia','europa','oceania','africa','antartida')}
print(var23) """
# 24) Imprimir las claves del diccionario
""" print(var23.items()) """
# 25) Imprimir las ciudades a través de su clave
""" print(var23['ciudad']) """