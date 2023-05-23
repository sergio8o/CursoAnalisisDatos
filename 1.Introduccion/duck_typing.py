'''
    El duck typing o tipado de pato es un concepto relacionado a la programacion orientada a objetos
    que aplica a ciertos lenguajes orientados a objetos y que tiene origen en la siguiente frase:
        Si camina como pato y habla como pato, entonces  debe ser un pato
    Se trata de un simil en el que los patos son objetos y hablar o caminal son metodos,
    es decir si un objeto tiene los metodos que necesitamos esto nos basta, siendo su tipo irrelevante

    En otras palabras, no te fijes si es un pato, fijate si camina como un pato, si habla como una pato, etc
    Si cumple con todas estas caracteristicas ¿ no se puede decir acaso que se trata de un pato?

    El concepto de duck typing se fundamenta en el razonamiento inductivo, donde una serie de premisas apoyan
     la conclusión, pero no la garantizan. Si vemos a un animal que parece un pato, habla como tal y anda como
      tal, sería razonable pensar que se trata de un pato, pero sin un test de ADN nunca estaríamos al cien por
       cien seguros.

    A python le da igual los tipos de los objetos, lo unico que le importan son los metodos

    Definamos una clase Pato con un método hablar().
    class Pato:
        def hablar(self):
            print("¡Cua!, Cua!")

    Y llamamos al método de la siguiente forma.
        p = Pato()
        p.hablar()
        # ¡Cua!, Cua!

    Hasta aquí nada nuevo, pero vamos a definir una función llama_hablar(), que llama al método hablar() del objeto
    que se le pase.
    def llama_hablar(x):
        x.hablar()

    Como puedes observar, en Python no es necesario especificar los tipos, simplemente decimos que el parámetro de
    entrada tiene el nombre x, pero no especificamos su tipo.

    Cuando Python entra en la función y evalúa x.hablar(), le da igual el tipo al que pertenezca x siempre y cuando
     tenga el método hablar(). Esto es el duck typing en todo su esplendor.

    p = Pato()
    llama_hablar(p)
    # ¡Cua!, Cua!
    ¿Y qué pasa si usamos otros objetos que no son de la clase Pato? Pues bien, como hemos dicho, a la función
     llama_hablar() le da igual el tipo. Lo único que el importa es que el objeto tenga el método hablar().


    Definamos tres clases de animales distintas que implementan el método hablar(). Nótese que no existe herencia
     entre ellas, son clases totalmente independientes. De haberla estaríamos hablando de polimorfismo.

    class Perro:
        def hablar(self):
            print("¡Guau, Guau!")

    class Gato:
        def hablar(self):
            print("¡Miau, Miau!")

    class Vaca:
        def hablar(self):
            print("¡Muuu, Muuu!")

    Y como es de esperar la función llama_hablar() funciona correctamente con todos los objetos.

        llama_hablar(Perro())
        llama_hablar(Gato())
        llama_hablar(Vaca())

    # ¡Guau, Guau!
    # ¡Miau, Miau!
    # ¡Muuu, Muuu!
    Otra forma de verlo, es iterando una lista con diferentes animales, donde animal va tomando los valores de cada objeto animal.
    Todo un ejemplo del duck typing y del tipado dinámico en Python.

    lista = [Perro(), Gato(), Vaca()]
    for animal in lista:
        animal.hablar()

    # ¡Guau, Guau!
    # ¡Miau, Miau!
    # ¡Muuu, Muuu!
'''

'''
    Ejemplos Duck Typing
    Ejemplo len()
    Podemos ver el duck typing en todo su esplendor con la función len(). 
    Dicha función lo único que realiza por debajo es llamar al método mágico __len__().
    Definamos dos clases:

    Foo implementa el método __len__().
    Bar no lo implementa.
    class Foo():
        def __len__(self):
            return 99
    
    class Bar():
        pass
    
    Ca la función len() no le importa el tipo del objeto que se le pase, siempre y cuando tenga el método __len__() 
    implementado. Por ello, en el segundo caso falla.

    print(len(Foo())) # 99
    print(len(Bar())) # Error


    Ejemplo multiplicar
    Por otro lado, cuando hacemos una multiplicación utilizando el operador aritmético * el resultado depende de
     los tipos que estemos usando.
    
    No es lo mismo multiplicar dos enteros que un entero y cadena.
    
    print(3*3)   # 9
    print(3*"3") # 333
    Una vez más, podemos ver el duck typing en Python. Simplemente se busca que los objetos a la izquierda y 
    derecha del * tengan implementado el __rmul__ o __mul__.
'''

'''
    Conclusiones
    Python es un lenguaje que soporta el duck typing, lo que hace que el tipo de los objetos no sea tan relevante, 
    siendo más importante lo que pueden hacer (sus métodos).
    
    Otros lenguajes como Java no soporta el duck typing, pero se puede conseguir un comportamiento similar cuando los 
    objetos comparten un interfaz (si existe herencia entre ellos). Este concepto relacionado es el polimorfismo.
    
    El duck typing está en todos lados, desde la función len() hasta el uso del operador *.

'''