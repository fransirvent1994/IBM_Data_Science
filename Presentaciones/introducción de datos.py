#En cuanto a crear variables, la mejor manera y más libre es jugar con "input()". Explico.
# Con input() podemos introducir los datos que veamos necesarios para el desarrollo del código en su output.
# De esta manera, no nos limitamos a que la variable valga una cosa determinada, sino que valdrá lo que mandemos en el output.
# Ejemplos:

x = input()
print(x)

# Con esto, el terminal nos pedirá que introduzcamos un valor, pero no hay mensaje ni resultado.
# Dandole algo de valor sería:

y = input("Introduce un número: ")
z = input("Introduce un segundo número: ")
resultado = y + z
print(f"El resultado de {y} + {z} es: {resultado}")
# Se usa f"{}" tras print para poder hacer uso de las variables en la salida del código. 

"""Esto no es del todo optimo para operaciones matemáticas, dado que los inputs son strings, y las operaciones matemáticas son
floats o ints, por lo que sucede que hay que corregir mediante transformación del tipo de valor, agregando int() a input, por
lo que quedaría como lo que sigue, cambiando las variables para que se note la diferencia de resultados entre el código de arriba
y el siguiente."""

y1 = int(input("Introduce un número: "))
z1 = int(input("Introduce un segundo número: "))
resultado1 = y1 + z1
print(f"El resultado de {y1} + {z1} es: {resultado1}")

# Con esto se puede ver que la diferencia entre el de arriba y el de abajo es el tipo de valor.
# Los strings no se pueden sumar, pero si combinar, lo que quiere decir que 2 + 2 no será 4, sino 22
# En cambio, los floats o ints si que se podrán sumar.
# Esto es un dato a tener en cuenta para llevar cuidado.

# Vamos con inputs sin matemáticas.

persona1 = "Ariel"
persona2 = input("Como te llamas? \n") #Usamos \n para hacer salto de línea
persona3 = "Jorge"
# Aquí tenemos 2 variables con nombres (strings) ya predeterminados, y una variable con input, donde puedes introducir cualquier nombre

# Aquí puedes jugar a introducir el nombre que quieras, por ejemplo, tu nombre.
pregunta = input("Quién se comió mi postre? \n")

# Aquí un ejemplo de resultado con condicionales if, elif y else, para mayor extensión de este apartado y profundidad de condicionales
if pregunta == persona2:
    print("Espero que seas intolerante a la lactosa")
elif pregunta == persona1 or pregunta == persona3:
    print("Ah, bueno, me cae bien")
else:
    print("Cobraré mi venganza, en esta vida o en la otra")