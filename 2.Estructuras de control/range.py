'''
    Una de las iteraciones mas comunes que se realizan, es la de iterar un numero de veces como 0  y n
    Con la estructura que debe seguir un for en pYTHON, para recorrer una variable i de 0 a 5( posiciones de un iterable)
    debo tener un estructura indexable con 5 elementos
    for i in (0,1,2,3,4,5)
        print(i) #0 1 2 3 4 5
    lo que se encuentra luego de in ,debe ser de la clase Iterable como la tupla del ejem
    se puede conseguir la misma tupla con range(6) (0,1,2,3,4,5)
    El range() genera una secuencia de números que van desde 0 por defecto hasta el número que se pasa como parámetro menos 1.

    e pueden pasar hasta tres parámetros separados por coma, donde el primer es el inicio de la secuencia,
     el segundo el final y
     el tercero el salto que se desea entre números. Por defecto se empieza en 0 y el salto es de 1.
    Por lo tanto, si llamamos a range() con (5,20,2), se generarán números de 5 a 20 de dos en dos.
     Un truco es que el range() se puede convertir en list.

    print(list(range(5, 20, 2)))

    Y mezclándolo con el for, podemos hacer lo siguiente.

    for i in range(5, 20, 2):
        print(i) #5,7,9,11,13,15,17,19

    Se pueden generar también secuencias inversas, empezando por un número mayor y terminando en uno menor, pero para ello el salto deberá ser negativo.
    for i in range (5, 0, -1):
        print(i) #5,4,3,2,1
'''