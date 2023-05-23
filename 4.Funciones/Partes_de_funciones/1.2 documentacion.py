'''
Ahora que ya tenemos nuestras propias funciones creadas, tal vez alguien se interese en ellas y podamos compartírselas. Las funciones pueden ser muy complejas, y leer código ajeno no es tarea fácil. Es por ello por lo que es importante documentar las funciones. Es decir, añadir comentarios para indicar como deben ser usadas.
'''
def mi_funcion_suma(a, b):
    """
    Descripción de la función. Como debe ser usada,
    que parámetros acepta y que devuelve
    """
    return a+b
'''
    Para ello debemos usar la triple comilla """ al principio de la función. Se trata de una especie de comentario que podemos usar para indicar como la función debe ser usada. No se trata de código, es un simple comentario un tanto especial, conocido como docstring.

    Ahora cualquier persona que tenga nuestra función, podrá llamar a la función help() y obtener la ayuda de como debe ser usada.

'''
help(mi_funcion_suma)

#  Otra forma de acceder a la documentación es la siguiente.

print(mi_funcion_suma.__doc__)