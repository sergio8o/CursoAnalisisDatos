'''
    Los conceptos de paso de valor o referencia son usados cuando se ve
    como las funciones tratan a los argumentos pasados como entrada.
    + Si usamos un argumento cuyo contenido se pasa por valor, se creara una copia
    local de la variable, lo que implica que cualquier modificacion sobre el mismo
    no tendrá efecto sobre el original.
    + Con una variable pasada como referencia, se actuara directemente sobre la 
    variable pasada, por lo que las modificaciones afectaran a la variable original.

    En python las cosas son diferentes, el comportamiento de las funciones con los
    argumentos estará definido por el tipo de variable con la que estemos trabajando.

'''
x = 10
def funcion(entrada):
    entrada = 0
funcion(x)
print(x)

'''
    Iniciamos la x a 10 y se la pasamos a funcion(). Dentro de la función hacemos que la variable valga 0. Dado que Python trata a los int como pasados por valor, dentro de la función se crea una copia local de x, por lo que la variable original no es modificada.
'''
'''
    No pasa lo mismo si por ejemplo x es una lista como en el siguiente ejemplo. En este caso Python lo trata como si estuviese pasada por referencia, lo que hace que se modifique la variable original. La variable original x ha sido modificada.
'''
'''x = [10, 20, 30]
def funcion(entrada):
    entrada.append(40)

funcion(x)
print(x) # [10, 20, 30, 40]'''
'''
    El ejemplo anterior nos podría llevar a pensar que si en vez de añadir un elemento a x, hacemos x=[], estaríamos destruyendo la lista original. Sin embargo esto no es cierto.
'''
x = [10, 20, 30]
def funcion(entrada):
    entrada = []

funcion(x)
print(x)
# [10, 20, 30]

'''
Una forma muy útil de saber lo que pasa por debajo de Python, es haciendo uso de la función id(). Esta función nos devuelve un identificador único para cada objeto. Volviendo al primer ejemplo podemos ver como los objetos a los que “apuntan” x y entrada son distintos.
'''

x = 10
print(id(x)) # 4349704528
def funcion(entrada):
    entrada = 0
    print(id(entrada)) # 4349704208

funcion(x)
'''
    Sin embargo si hacemos lo mismo cuando la variable de entrada es una lista, podemos ver que en este caso el objeto con el que se trabaja dentro de la función es el mismo que tenemos fuera.
'''
x = [10, 20, 30]
print(id(x)) # 4422423560
def funcion(entrada):
    entrada.append(40)
    print(id(entrada)) # 4422423560

funcion(x)