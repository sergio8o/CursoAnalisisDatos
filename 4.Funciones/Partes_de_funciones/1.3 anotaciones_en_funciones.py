'''
    Existe una funcionalidad relativamente reciente en Python llamada function annotation o anotaciones en funciones. Dicha funcionalidad nos permite añadir metadatos a las funciones, indicando los tipos esperados tanto de entrada como de salida.  
'''
def multiplica_por_3(numero: int) -> int:
    return numero*3

multiplica_por_3(6) # 18
'''
    Las anotaciones son muy útiles de cara a la documentación del código, pero no imponen ninguna norma sobre los tipos. Esto significa que se puede llamar a la función con un parámetro que no sea int, y no obtendremos ningún error.
'''
multiplica_por_3("Cadena")
# 'CadenaCadenaCadena'