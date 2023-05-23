'''
    Como ya se vio python tiene un conjunto de palabras reservadas que no se pueden usar para
    nombrar variables o funciones, ya que las reserva internamente para su funcionamiento.
    Por ejm no se puede usar una funcion llamada True, porque se tendria un error de Sintaxis
    De ser posible se podria romper el lenguaje
    Algo muy importante es saber que las palabras como list() no estan reservadas y esto
    puede generar problemas
    Este codigo genera una lista y la guarda en 'a' a partir de un String, cadena de caracteres
    a = list("letras")
    print(a)
    # ['l', 'e', 't', 'r', 'a', 's']

    Se puede crear una funcion con ese nombre, con esto se esta eliminando o reemplazando la funcion
    list() de Python y por lo tanto al intentar realizar de nuevo la llamada anterior esta falla
    ya que nuestra funcion no acepta argumentos

    def list():
    print("Funcion list")

    a = list("letras")
    # TypeError: list() takes 0 positional arguments but 1 was given

    import keyword Con este comando se puede acceder a la lista de palabras reservadas
    print(keyword.kwlist


'''