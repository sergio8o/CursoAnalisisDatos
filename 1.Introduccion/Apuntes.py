'''
    Python es independiente de OS que se este usando bien puede ser Linux, Windows o Mac. Es multiplataforma
    por lo que el codigo es compatible con cualquier plataforma.
    Python es de proposito general, se puede desarrollar varios tipos de sistemas
    Python tiene mucha simplicidad de lenguaje
    Es de tipado dinamico y tambien es un lenguaje interpretado
    Ni bien creamos el codigo se va interpretando para la computadora
    Se crea un archivo main al crear el proyecto, el nombre del archivo puede ser otro
    Se crean ambientes virtuales
    Es facil de aprender
    LA NASA, NETFLIX, YOUTUBE Y DEMAS USAN PYTHON
    Python se usa para el desarrrollo web con framework como Django,Pyramid , flask o bottle que permiten
    desarrollar paginas a todos los niveles.
    Desarrollo de software: es usado como soporte para desarrolladores como para testing
    Machine learning: Crece el numero de librerias en python para el aprendizaje automatico como
    Keras, tensorflow, pytorch o sklearn
    Visualizacion de datos: existen muchas librerias muy usadas para mostrar datos en graficas, como
    matplotlib, seaborn y plotly

    CARACTERISTICAS
    Python tiene caracteristicas que lo hacen diferente del resto
    1. es un lenguaje interpretado, no compilado
    2. usa tipado dinamico, lo que significa que una variable puede tomar valores de distinto tipo
    3. es fuertemente tipado, lo que significa que el tipo no cambia de manera repentina, tiene que hacer
    una conversion explicita    .
    4. Es multiplataforma
    Adicional: En otros lenguajes se tiene que indicar el tipo de los parametros de sus funciones, en python
    la funcion acepta un parametro de entrada pero no se especifica su tipo
    La funcion es llamada con un int, pero su valor se divide entre 2 y el resultado es convertido automaticamente
    en un float.

    def funcion(entrada):
    return entrada/2

    x = "Hola"
    x = 7.0
    x = int(x)
    x = funcion(x)
    print(x)
    print(type(x))

    # 3.5
    # <class 'float'>

    Todo en python es un funcion, incluso una funcion pertenece a una clase function

    El lenguaje Python es conocido por ser tanto de tipado dinámico como fuertemente tipado.
    El tipado dinámico significa que las variables no están asociadas a un tipo de datos
    específico durante la compilación, sino que su tipo se determina en tiempo de ejecución.
    Por otro lado, el tipado fuerte se refiere a la restricción de realizar operaciones entre
    tipos incompatibles sin una conversión explícita.

    Aquí tienes algunos ejemplos que demuestran el carácter fuertemente tipado de Python:

    1.Concatenación de cadenas y enteros:
    cadena = "Hola"
    numero = 42
    concatenacion = cadena + numero  # Esto generará un error de tipo
    En este ejemplo, intentamos concatenar una cadena de texto con un entero. Python no permite
    la concatenación directa entre estos tipos y generará un error de tipo.

    2.Operaciones aritméticas con tipos incompatibles:
    numero = 42
    texto = "10"
    resultado = numero + texto  # Esto generará un error de tipo
    En este caso, estamos intentando sumar un entero con una cadena que representa un número.
     Python no permite la operación directa entre estos tipos y producirá un error de tipo.

    3.Comparación de tipos distintos:
    numero = 42
    booleano = True
    comparacion = numero > booleano  # Esto generará un error de tipo
    Aquí intentamos comparar un entero con un valor booleano. Python no permite la comparación
    directa entre tipos incompatibles y arrojará un error de tipo.

    Python, a pesar de ser un lenguaje de tipado dinámico, sigue siendo fuertemente tipado. Requiere
    que los tipos de datos sean compatibles para realizar operaciones y comparaciones, y solo realiza
    conversiones automáticas en ciertos casos, pero no entre tipos distintos sin una conversión explícita


'''

'''
    The Zen of Python: coleccion de 19 principios que influyen en diseño del lenguaje
    Solo las que tienen logica para mi
    1. Bello es mejor que feo
    2. Explicito es mejor que implicito
    3. Simple es mejor que complejo
    4. Complejo es mejor que complicado
    5. La legibilidad es importante
    6. Los casos especiales no son lo suficientemente especiales para romper las reglas
    7.Los errores nunca deben pasar silenciosamente
    8.A MENOS QUE SE SILENCIEN EXPLICITAMENTE
    9. Frente a la ambiguedad, evitar la tentacion a adivinar.
    10. Si la implementacion es dificil de explicar entonces en mala idea
    11. Si la implementacion es facil de implemente, puede que sea una buena idea.
    12. Los namespaces son buena idea, mas de esos por favor.


    Con # se tiene texto que acompaña al codigo, pero este texto no es codigo .Son anotaciones del codigo
    que puede ser util para otras personas o para mi yo futuro ya que representa informacion relevante acerca del codigo.
    Para python el comentario no existe, por que no es codigo.
    Comentario de una linea con : #
    Comentario de varias lineas con: 2 pares de 3 comillas simple
 
    
    
    Python no necesita que le digas explicitamente el tipo de dato que guardara la variable
    Python es inteligente y el detecta cual es según lo que se ha almacenado
    En python se pueden guardar valores numericos entero, con parte decimal indicados con un . , cadenas de texto
    que se encuentran entre comillas simples o dobles, tambien valores booleanos
    
    
    SINTAXIS
    La sintaxis hace referencia al conjunto de reglas que definen como se tiene que escribir el codigo
    en un determinado lenguaje de programacion. Es la forma en que se debe escribir para que el lenguaje
    de programacion nos entienda. Y dile a la computadora que haga, esto y esto y este.. . py:que dice aqui?
    
    En la mayoria de los lenguajes existen una sintaxis comun, como el uso de "=" o el uso de {} para indicar
    bloques de  codigo, conjunto de lineas de codigo asociados.
    
    La sintaxis es a la programacion lo que la gramatica es a los idiomas.
    De la misma forma que la frase “Yo estamos aquí” no es correcta, el siguiente código en Python no sería correcto,
     ya que no respeta las normas del lenguaje.

    if ($variable){
        x=9;
    }
    
    Al igual que un lenguaje no se habla con simplemente saber todas sus palabras, en programacion no basta con
    saber la sintaxis de un lenguaje para programar correctamente en el. Es cierto que sabiendo la sintaxis
    se puede empezar a programar y hacer todo lo que se quiera pero el lenguaje python va mas alla.
    
    
    IDENTACION
    Los bloques de codigo o todo el codigo asociado a una determinada funcion se representa mendiante un tabulador
    o espacios, la norma general es usar 4 espacios
    A todo funcion condicional ,repetitiva ,o la que sea debe tener asociado un bloque de codigo. sino hay error
    
    A diferencia de otros lenguajes no es necesario usar; para terminar cada linea basta con un salto de linea
    x = 10;

    x = 5
    y = 10
    
    Pero se puede usar el punto y coma ; para tener dos sentencias en la misma línea.
    x = 5; y = 10
    
    
    Multiples lineas
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx (79 caracteres 'x')
    En muchas ocasiones se puede necesitar que una instruccion se encuentre en varias lineas de codigo. Como
    principal motivo que la linea sea muy larga, una recomendacion es que las lineas no excedan de 79 caracteres.
    
    Haciendo el uso de \ se puede romper el codigo en varias lineas, lo que en determinados
    casos hace que el codigo sea mas legible
    x = 1+2+3+4+5+\
        6+7+8
    
    
    Si por lo contrario estamos dentro de un bloque rodeado con paréntesis (), bastaría con saltar a la siguiente línea.
    x = (1 + 2 + 3 + 4 +
         5 + 6 + 7 + 8)
    Se puede hacer lo mismo para llamadas a funciones
    def funcion(a, b, c):
        return a+b+c
    
    d = funcion(10,
    23,
    3)
    
    
    CREANDO VARIABLES
    Ya se sabe como crear , se le tiene que dar un nombre y asignarle un valor con '="
    asi nomas se le asigna un valor a un nombre sin necesidad de haberlo creado antes
    Otras formas
    x = y = z = 10
    Tambien se pueden asignar varios valores separados por comas, una variable solo puede tener un valor
    x , y = 2, 10
    x, y, z = 2, 10 ,14
    
    
    NOMBRANDO VARIABLES
    Se les puede llamar como quiera, pero debo recordar que python es sensitiveCase o sea disitingue en mayusculas
    y minusculas. Las variables x y X son distintas
    Existen normas para llamar a un funcion
    El nombre no puede empezar por un numero
    No se permite el uso de guiones, solo guiones bajos
    No se permite el uso de espacios en los nombres
    
    # Válido
    _variable = 10
    vari_able = 20
    variable10 = 30
    variable = 60
    variaBle = 10
    
    # No válido
    2variable = 10
    var-iable = 10
    var iable = 10
    
    La ultima condicion para nombrar variables, es no usar nombres reservados para Python.
    Las palabras reservadas son usadas por Python internamente para sus propositos, por lo que 
    no se puede usar para nuestras variables y funciones
    
    import keyword    con este comando se puede ver todas las palabras clave que no se puede usar.
    print(keyword.kwlist) 
    
    # ['False', 'None', 'True', 'and', 'as', 'assert',
    # 'async', 'await', 'break', 'class', 'continue',
    # 'def', 'del', 'elif', 'else', 'except', 'finally',
    # 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    # 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
    # 'return', 'try', 'while', 'with', 'yield']
    
    USO DE PARENTESIS
    Python soporta todos los operadores matematicos mas comunes, +  / * y exponenciacion **
    y otros mas
    Los parentesis tambien se usan, en python el orden por prioridad al momento de resolver operaciones
    se mantiene e incluyen a los parentesis, aquellas operaciones entre parentesis son aquellas con mayor prioridad
    
    VARIABLES Y ALCANCE: esto se vera mejor en el tema de funciones
    cuando definimos una variable, es saber el alcance o scope que tiene. En el siguiente ejemplo la variable con valor 
    10 tiene un alcance global y la que tiene el valor 5 dentro de la función, tiene un alcance local. Esto significa q
    ue cuando hacemos print(x), estamos accediendo a la variable global x y no a la x definida dentro de la función.
    
    x = 10

    def funcion():
        x = 5
    
    funcion()
    print(x)
    Es util sabe lo que va pasando un programa a medida que se va ejecutando sus instrucciones 
    ello se hace uso de instrucciones print()
    Existen muchas formas de usar la funcion print()
    ESO SE VERA EN CADENAS DE PYTHON
    
    
    
    
'''
