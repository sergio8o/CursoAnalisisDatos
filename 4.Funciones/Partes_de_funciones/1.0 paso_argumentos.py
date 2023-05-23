'''
    Las funciones representan acciones por la computadora con datos
    Existen aquellas que son construidas por Python y aquellas que son definidas por mi
    Se usa def para definir los metodos
    def nombre_funcion(lista de parametros):
        codigo
        return valor_retornado
    Todas las funciones tienen un nombre, argumentos de entrada, codigo a ejectuar y unos
    parametros de salida. Es analogo con las funciones matematicas, estas reciben numeros
    como entrada y devuelve su respectivo valor de salida el cual depende de como se definio
    la funcion. 
    Las funciones fueron creadas a partir de los siguientes principios:
    Reusabilidad: que nos dice que si tenemos un fragmento de codigo usado en varias partes
    del programa, la mejor solucion seria pasarlo a una funcion. Esto nos permite evitar
    tener codigo repetido y que modificarlo fuera mas facil ya que bastaria con cambiar la 
    funcion una vez.

'''
'''
    Tipos de funciones
    Funcion sin parametros
    Funcion con un parametro

    Python permite pasar argumentos de otras formas
    Argumentos por posicion:
    def resta(a, b):
        return a-b
    resta(5, 3) # 2
    Al tratarse de parámetros posicionales, se interpretará que el primer número es la a y 
    el segundo la b. El número de parámetros es fijo, por lo que si intentamos llamar a la
    función con solo uno, dará error. TypeError
    Tampoco es posible usar mas argumentos de los tiene la función definidos, ya que no sabría 
    que hacer con ellos.


    Argumentos por nombre:
    Pasar argumentos por nombre a una funcion es una forma legible de llamar a una funcion
    cuando hay varios argumentos y saber que valor le corresponde a cada parametro.

    imprimir_factura(nombre_cliente="Juan Perez", direccion_envio="Calle 123, Ciudad",
      cantidad_total=1000, fecha_factura="2023-05-05")

    Además, pasar argumentos por nombre puede ser útil en situaciones en las que solo se desea
    proporcionar valores para algunos de los argumentos de una función, y dejar que los valores
      predeterminados se utilicen para los demás. 

      Supongamos que tenemos una función llamada calculadora que realiza una operación 
      aritmética básica entre dos números y tiene tres argumentos: num1, num2 y operacion.
      Si el argumento operacion no se proporciona, se utiliza el valor predeterminado
      "sumar".
'''
#Tecnica de pasar por nombre los argumentos para proporcionar valores solo a algunos 
#parametros y dejar que usen los valores predeterminados para los demas
#Si el argumento operacion no se proporciona se pasa el valor predeterminado sumar
def calculadora(num1, num2, operacion="sumar"):
    if operacion == "sumar":
        resultado = num1 + num2
    elif operacion == "restar":
        resultado = num1 - num2
    elif operacion == "multiplicar":
        resultado = num1 * num2
    elif operacion == "dividir":
        resultado = num1 / num2
    else:
        print("Operación no válida")
        return
    
    print("El resultado es:", resultado)
    return resultado


# Llamando a la función con valores para todos los argumentos
calculadora(num1=5, num2=3, operacion="restar")   # resultado: 2

# Llamando a la función con solo num1 y num2 proporcionados
calculadora(num1=5, num2=3)   # resultado: 8 (suma predeterminada)

# Llamando a la función con solo num2 proporcionado
calculadora(num2=3)   # resultado: TypeError: calculadora() missing 1 required
#positional argument: 'num1'


'''
    Argumentos por defecto
    Tal vez queramos tener una funcion con algun parametro opcional, que pueda
    ser usado o no dependiendo de diferentes circunstancias. Para ello, lo que 
    se puede hacer es asignar un valor por defecto al parametro
    En el siguiente ejm c valdria cero en caso no se indique lo contrario
'''
def sumar(a, b, c=0):
    return a+b+c
sumar(5,5,3) # 13
#Dado que el parámetro c tiene un valor por defecto, la función puede ser llamada sin ese valor.
sumar(4,3) # 7

#Podemos incluso asignar un valor por defecto a todos los parámetros, por lo que se podría 
# llamar a la función sin ningún argumento de entrada.
def suma(a=3, b=5, c=0):
    return a+b+c
suma() # 8

#Las siguientes llamadas a la función también son válidas

suma(1)     # 6
suma(4,5)   # 9
suma(5,3,2) # 10
#O haciendo uso de lo que hemos visto antes y usando los nombres de los argumentos.

suma(a=5, b=3) #8

'''
    Argumentos de longitud variable
    En el ejemplo con argumentos por defecto, hemos visto que la función puede ser llamada con diferente número de argumentos de entrada, pero esto no es realmente una función con argumentos de longitud variable, ya que existe un número máximo.
    Imaginemos que queremos una función suma() como la de antes, pero en este caso necesitamos que sume todos los números de entrada que se le pasen, sin importar si son 3 o 100. Una primera forma de hacerlo sería con una lista.

    def suma(numeros):
    total = 0
    for n in numeros:
        total += n
    return total
    suma([1,3,5,4]) # 13

    La forma es válida y cumple nuestro requisito, pero realmente no estamos trabajando con argumentos de longitud variable. En realidad tenemos un solo argumento que es una lista de números.

    Por suerte, Python tiene una herramienta muy potente. Si declaramos un argumento con *, esto hará que el argumento que se pase sea empaquetado en una tupla de manera automática. No confundir * con los punteros en otros lenguajes de programación, no tiene nada que ver.

    def suma(*numeros):
    print(type(numeros))
    # <class 'tuple'>
    total = 0
    for n in numeros:
        total += n
    return total
    suma(1, 3, 5, 4) # 13

    El resultado es igual que el anterior, y podemos ver como efectivamente numeros es de la clase tuple. También podemos hacer otras llamadas con diferente número de argumentos

    suma(6) # 6
    suma(6, 4, 10) # 20
    suma(6, 4, 10, 20, 4, 6, 7) # 57

    Usando doble ** es posible también tener como parámetro de entrada una lista de elementos almacenados en forma de clave y valor. En este caso podemos iterar los valores haciendo uso de items().


    def suma(**kwargs):
    suma = 0;
    for key, value in kwargs.items():
        print(key, value)
        suma += value
    return suma

    suma(a=5, b=20, c=23) # 48


    De igual manera, podemos pasar un diccionario como parámetro de entrada.

    def suma(**kwargs):
        suma = 0
        for key, value in kwargs.items():
            print(key, value)
            suma += value
        return suma
    di = {'a': 10, 'b':20}
    suma(**di) # 30 NO CREO QUE SEA NECESARIO EL DOBLE ASTERISCO
'''