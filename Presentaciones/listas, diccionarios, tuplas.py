# Las listas es la manera que tenemos de tener una cantidad de valores y que, además, se puedan modificar.
# Ejemplo de lista

lista = ["A", "B", "C"]
print(lista)

# Tenemos como resultado que imprime los tres carácteres, pero podemos acceder a ellos para modificarlos, eliminar, o añadir.
# Añadir
lista.append("D")
print(lista)

# Ahora el resultado muestra la D al final de la lista

# Eliminar
lista.remove("B")
print(lista)

# Esto eliminará la B como resultado

# Las listas son modificables, en cambio, las tuplas no

# Ejemplo de tuplas

tupla = ("A", "B", "C")
print(tupla)

# Al ser inmutables, no puedes modificarlas, pero si acceder a ellas. Por ejemplo, si queremos ver que cantidad de valores tiene la tupla
print(len(tupla))
# Que valor hay en el hueco 2
print(tupla[1]) # Los contenedores van desde el 0, por lo que el hueco número 2 no es el 2, sino el 1, dado que empieza a contar desde 0

# Los diccionarios son contenidos de información que almacenan variables y valores dentro de un diccionario.
# Ejemplo de diccionario

mi_diccionario = {"A" : 2, "B" : 3}
print(mi_diccionario)

# Puedes acceder a estos valores de diversas formas.
print(mi_diccionario["A"])  # Imprimirá 2
print(mi_diccionario["B"])  # Imprimirá 3