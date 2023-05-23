'''
    Un programa es un conjunto de instrucciones usadas para realizar algo en especifico
    o resolver un problema informatico
    El flujo de ejecucion de las instrucciones es de arriba hacia abajo

    De no ser por las estructuras de control, el codigo en cualquier lenguaje
    de programacion seria ejecutado desdse arriba hasta abajo secuencialmente hasta terminar.
    Un codigo no deja de ser un conjunto de instruccion ejecutadas una tras otra.
    Con una estructura de control se puede cambiar el flujo de ejecucion de un programa.
    haciendo que ciertos bloques se ejecuten si y solo si se cumplen determinadas condiciones

    USO DEL IF (estructura de control condicional)
    se usa para asegurarse que se cumplen ciertas condiciones necesarias para la correcta ejecucion
    del codigo o el cumplimiento de la tarea.
    para una division Si el denominador es cero entonces no se debe realizar la division
    a= 1
    b = 0
    if b != 0:      La sentencia if debe ir terminado por : y el bloque de codigo a ejecutar debe estar identado.
        print(a/b)
    Todas las lineas de codigo que esten despues del if y esten identadas entonces pertenecen al condicional
    bloque de codigo que se ejecutara si la condicion se cumple

    Dentro de un if se usan operadores relacionales, que indican la relacion entre valores normalmente numericos
    aunque tambien puede haber comparaciones entre tipos de datos diferentes como boolenaos,strings,caracteres,etc.

    En la cabecera de la estructura if, pueden haber varias condiciones unidas por conectores logicos
    a = 10
    if a > 5 and a <15
        print("El numero es mayor que 5 y menor que 15")

    Si tenemos un if sin contenido, tal vez porque todavia no sabemos que colocar ahi podemos dejarlo en pendiente
    usando la palabra pass. Realmente pass no hace algo , solo es para tener contento al interpretador de codigo
    if a > 5:
        pass

    Algo no demasiado recomendable pero que es posible, es poner todo el bloque que va dentro del if en la misma línea,
     justo a continuación de los :. Si el bloque de código no es muy largo, puede ser útil para ahorrarse alguna línea
      de código.

      if a > 5: print("Es > 5")

   Si tu bloque de código tiene más de una línea, se pueden poner también en la misma línea separándolas con ;.
   if a > 5: print("Es > 5"); print("Dentro del if")
'''

'''
    Uso del else y elif
    Es posible que no solo queramos hacer algo si una determinada condicion se cumple, sino que ademas
    se necesita hacer algo en caso no se cumpla. Es aqui donde se usa la clausula else.
    La parte del if se comporta igual, ahora se le agrega el bloque del else que se ejecutara si el bloque
    del if no lo hace porque no se cumplio la condicion. Entonces si o si se ejecutara un bloque de codigo.
    
    x = 5
    if x == 5:
        print("Es 5")
    else:
        print("No es 5")
        
    
    Si se tiene varias condiciones diferentes y para cada uno se necesita codigo distinto. es aqui
    donde entra en juego el elif
    
    x = 5
    if x == 5:
        print("Es 5")
    elif x == 6:
        print("Es 6")
    elif x == 7:
        print("Es 7")
        
    Con la cláusula elif podemos ejecutar tantos bloques de código distintos como queramos según la condición. 
    Traducido al lenguaje natural, sería algo así como decir: si es igual a 5 haz esto, si es igual a 6 haz lo otro, 
    si es igual a 7 haz lo otro.

    Se puede usar también de manera conjunta todo, el if con el elif y un else al final. Es muy importante notar que if
     y else solamente puede haber uno, mientras que elif puede haber varios.
    
    x = 5
    if x == 5:
        print("Es 5")
    elif x == 6:
        print("Es 6")
    elif x == 7:
        print("Es 7")
    else:
        print("Es otro")
    Si vienes de otros lenguajes de programación, sabrás que el switch es una forma alternativa de elif,
     sin embargo en Python esta cláusula no existe.
'''

'''
    Operador ternario
    El operador ternario o ternary operator es una herramienta muy potente que muchos lenguajes de programación tienen. 
    En Python es un poco distinto a lo que sería en C, pero el concepto es el mismo. Se trata de una cláusula if, else
     que se define en una sola línea y puede ser usado por ejemplo, dentro de un print().
     
     x = 5
    print("Es 5" if x == 5 else "No es 5")
    #Es 5
    
    Existen tres partes en un operador ternario, que son exactamente iguales a los que había en un if else. Tenemos 
    la condición a evaluar, el código que se ejecuta si se cumple, y el código que se ejecuta si no se cumple. 
    En este caso, tenemos los tres en la misma línea.

    # [código si se cumple] if [condición] else [código si no se cumple]
    
    Ahorra tiempo al escribir codigo, en casos de asignacion de una variable o para realizar una division
    un incremento o decremento, cosas simples
    
    a = 10
    b = 5
    c = a/b if b!=0 else -1
    print(c)
    #2
    
    Ejemplos if
    # Verifica si un número es par o impar
    x = 6
    if not x%2: ( si es cero, valor que se considera False en un contexto booleano entonces lo niego con not)
        print("Es par")
    else:
        print("Es impar")
        
    x = 5
    x-=1 if x>0 else x (en caso no sea positivo entonces se la reasigna el mismo valor) 
    print(x)
    
    Esto es lo mismo
    x = 5
    if x > 0:
        x -= 1
    else:
        x = x
    print(x)
'''
