from collections.abc import Iterable


'''
    El for es un tipo de bucle, donde el numero de repeticiones de bloque asociado esta determinado
    de antemano. Esta determinado por un objeto iterable que define las veces que se ejecutara el codigo.
    Un iterable es un objeto, que digamos tiene una longitud (cantidad de elementos) y que puede ser
    recorrido por un bucle for
'''

for i in "python":
    print(i)

#En cada iteracion i que es la variable de iteracion , se le asigna un valor del iterable
#La posicion del valor asignado del iterable, coincide con el numero de iteracion que se va realizando desde 0.

for i in range(0, 5):
    print(i)
# 0 1 2 3 4
#range es un metodo que devuelve un iterable, en este caso una estructura tupla cuyo valores van de 0 a 4 en ese orden.

'''
    ITERABLES E ITERADORES
    Que una estructura sea "iterable" significa que se puede recorrer de manera secuencial, accediendo a cada uno de sus
     elementos uno a la vez. En programación, la capacidad de iterar sobre una estructura de datos es fundamental para
    poder realizar operaciones repetitivas o acceder a los elementos almacenados en dicha estructura.

    En  Python, existen tipos de datos o estructuras de datos que son iterables, 
    como listas, tuplas, conjuntos y diccionarios. Al ser iterables, se puede utilizar un bucle para recorrer sus elementos 
    uno por uno para realizar tareas como procesamiento de datos, búsqueda, filtrado, entre otros.

    Los iteradores son objetos que hacen referencia a un elemento, y que tienen un método next que permite hacer referencia al siguiente.
    
    los iterables son objetos que pueden ser iterados o accedidos con un índice. 
    
    #for <variable> in <iterable>:
#    <Código>
    Yo creo que se puso un iterable como necesario para recorrer un bucle porque normalmente
    para esto se usan los bucles para recorrer estructuras de datos como arreglos, listas, tuplas, colas,pilas diccionarios, etc
    ahora si no es necesario porque se va a repetir una instrucciones que no tienen que ver con una estructura
    se puede usar range(# de repeticiones necesarias) y se tiene exactamente lo que se quiere.
    
    Como saber si algo es iterable?
    Con el metodo isinstance(), devuelve true si pertenece a la clase Iterable o false sino
    
    from collections import Iterable
    lista = [1, 2, 3, 4]
    cadena = "Python"
    numero = 10
    print(isinstance(lista, Iterable))  #True
    print(isinstance(cadena, Iterable)) #True
    print(isinstance(numero, Iterable)) #False
    
'''
'''
    La función isinstance() toma dos argumentos: el objeto que se quiere verificar (variable en este caso) 
    y la clase con la que se quiere comparar
'''
listaza = [1,2,3]
print(isinstance(listaza,Iterable))
numero = 200
print(isinstance(numero,Iterable))
print(isinstance(numero,int))
'''

REVISAR PARA ENTENDER MEJOR POO EN PYTHON
    El módulo collections.abc proporciona la clase abstracta Iterable, que es una clase base para todos los iterables 
    en Python. La función isinstance() se utiliza para verificar si un objeto es una instancia de una clase determinada
     o si es una instancia de una subclase de esa clase. Por lo tanto, isinstance(listaza, Iterable) devuelve True
    porque la lista listaza es un iterable, mientras que isinstance(numero, Iterable) devuelve False porque el número
    numero no es un iterable. La última línea isinstance(numero, int) devuelve True porque el número numero es una instancia de la clase int.
    
    collections.abc, que es un módulo en la biblioteca estándar de Python. abc significa "Abstract Base Classes" (Clases Base Abstractas).

    El módulo collections.abc proporciona una serie de clases abstractas que sirven como interfaces o superclases para
    varios tipos de datos en Python. Estas clases abstractas son útiles cuando deseas verificar si un objeto cumple 
    con ciertas características o comportamientos específicos.
    
    
    En el ejemplo anterior, importamos la clase abstracta Iterable del módulo collections.abc. La clase Iterable define
     una interfaz para los objetos que pueden ser recorridos con un bucle for. Al usar isinstance(objeto, Iterable), 
     podemos verificar si un objeto es iterable, es decir, si se puede iterar sobre él.

    El módulo collections.abc también proporciona otras clases abstractas útiles, como Container, Sized, Hashable, 
    entre otras, que te permiten realizar comprobaciones y asegurarte de que los objetos cumplen con ciertos protocolos
     o características específicas.

'''
'''
    ITERADORES:
    Para entender a los iteradores es necesario conocer la funcion iter(), esta funcion puede ser llamada
    sobre un objeto que sea iterable y nos devuelve un iterador para el mismo iterable.
    
    lista = [5, 6, 3, 2]
    it = iter(lista)
    print(it)       #<list_iterator object at 0x106243828>
    print(type(it)) #<class 'list_iterator'>
    
    it es un iterador, de la clase list_iterator. Esta variable iteradora, hace referencia a la lista original y
     nos permite acceder a sus elementos con la función next(). Cada vez que llamamos a next() sobre it, nos 
     devuelve el siguiente elemento de la lista original. Por lo tanto, si queremos acceder al elemento 4, tendremos
      que llamar 4 veces a next(). Nótese que el iterador empieza apuntando fuera de la lista, y no hace referencia
      al primer elemento hasta que no se llama a next() por primera vez.
      
      lista = [5, 6, 3, 2]
    it = iter(lista)
    print(next(it))
    #     [5, 6, 3, 2]
    #      ^
    #      |
    #     it
    print(next(it))
    #     [5, 6, 3, 2]
    #         ^
    #         |
    #        it
    print(next(it))
    #     [5, 6, 3, 2]
    #            ^
    #            |
    #           it
    
    Para saber mas: Existen otros iteradores para diferentes clases:

    str_iterator para cadenas
    list_iterator para listas.
    tuple_iterator para tuplas.
    set_iterator para sets.
    dict_keyiterator para diccionarios.
    
    Dado que el iterador hace referencia a nuestra lista, si llamamos más veces a next() que la longitud de la lista, 
    se nos devolverá un error StopIteration. Lamentablemente no existe ninguna opción de volver al elemento anterior.

    lista = [5, 6]
    it = iter(lista)
    print(next(it))
    print(next(it))
    #print(next(it)) # Error! StopIteration
    
    Es perfectamente posible tener diferentes iteradores para la misma lista, y serán totalmente independientes. 
    Tan solo dependerán de la lista, como es evidente, pero no entre ellos.

    lista = [5, 6, 7]
    it1 = iter(lista)
    it2 = iter(lista)
    print(next(it1)) #5
    print(next(it1)) #6
    print(next(it1)) #7
    print(next(it2)) #5
'''
print("\n\n")
string = "Sergio"
lista = [1,2,3,4,5]
tupla = (1,2,3,4,5)
diccionario = {1:"Hola",2:"Que tal",3:"Como estas"}

it = iter(string)
it2 = iter(lista)
it3 = iter(tupla)
it4 = iter(diccionario)
print(it) #iter(string) me devuelve un objeto iterador , y con print() se muestra su representacion en memoria
print(it2)
print(it3)
print(it4)

print(next(it)) #s
print(next(it)) #e
print(next(it)) #r
print(next(it)) #g
print(next(it)) #i


for iterador in string:
    print(iterador)

for iterador in lista:
    print(iterador)

for iterador in tupla:
    print(iterador)

for iterador in diccionario:
    print(iterador)
'''
For anidados
Es posible anidar los for, es decir, meter uno dentro de otro. Esto puede ser muy útil si queremos iterar algún objeto 
que en cada elemento, tiene a su vez otra clase iterable. Podemos tener por ejemplo, una lista de listas, una especie
 de matriz.

lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]
Si iteramos usando sólo un for, estaremos realmente accediendo a la segunda lista, pero no a los elementos individuales.

for i in lista:
    print(i)
#[56, 34, 1]
#[12, 4, 5]
#[9, 4, 3]


Si queremos acceder a cada elemento individualmente, podemos anidar dos for. 
Uno de ellos se encargará de iterar las columnas y el otro las filas.

for i in lista: Recorre las filas
    for j in i: Recorre las columnas
        print(j)
# Salida: 56,34,1,12,4,5,9,4,3
'''
listaSrg = ["Sergio","Alexander","Rojas", "Ledesma"]
for i in listaSrg:
    print(i)

for i in listaSrg:
    for j in i:
        print(j)

'''
    Ejemplos for
    Iterando cadena al revés. Haciendo uso de [::-1] se puede iterar la lista desde el último al primer elemento.
    
    texto = "Python"
    for i in texto[::-1]:
        print(i) #n,o,h,t,y,P
        
    Itera la cadena saltándose elementos. Con [::2] vamos tomando un elemento si y otro no.

    texto = "Python"
    for i in texto[::2]:
        print(i) #P,t,o
        
    Un ejemplo de for usado con comprehensions lists.
    print(sum(i for i in range(10)))
    # Salida: 45



    En Python, los dos puntos : dentro de los corchetes [] se utilizan para la segmentación (slicing) de secuencias, 
    como cadenas, listas o tuplas. La sintaxis general de la segmentación es [inicio:fin:paso],
     donde:
    
    inicio es el índice de inicio de la segmentación. Si se omite, se asume el inicio de la secuencia.
    
    fin es el índice de fin de la segmentación. Si se omite, se asume el final de la secuencia.
    
    paso es el incremento entre los índices. Si se omite, se asume un paso de 1.
    
    En el caso específico de texto[::-1], se utiliza la segmentación para crear una nueva secuencia que es una reversión de 
    la secuencia original texto. 
    
    Aquí está la explicación paso a paso:

    inicio se omite, por lo que se asume el inicio de la secuencia.
    fin se omite, por lo que se asume el final de la secuencia.
    paso se establece como -1, lo que significa que los índices se recorren en sentido inverso, desde el final hacia el inicio.
'''

