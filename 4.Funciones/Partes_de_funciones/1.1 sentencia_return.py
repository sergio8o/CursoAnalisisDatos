'''
    El uso de la sentencia return permite dos cosas:
    +Salir o termina la ejecucion de la funcion y transferir la ejecucion de vuelta
    a donde se realizo la llamada.
    +Devolver uno o varios parametros, fruto de la ejecucion de la funcion
    Respecto a lo primero, una vez se llama a return se para la ejecucion de la funcion
    y se vuelve o retorna al punto donde fue llamada. Es por ello que el codigo
    que esta despues de return no se ejecuta
'''
def mi_funcion():
    print("Entra en mi funcion")
    return
    print("No llega") #El mismo IDE me dice que esto no se ejecuta xq no le pertenece a nadie
    #por la sangria se entiende que le pertenece a la funcion pero como ya se termino con
    #return no le pertenece
mi_funcion()#Entra en mi funcion

'''
    Por esto tambien solo se llama a return una sola vez en la funcion, cuando ya se hizo
    que lo tenia que hacerse.
    Por otro lado, se pueden devolver parametros. Las funciones normalmente son llamadas
    para realizar calculos en base a una o varias entradas, por lo que es necesario
    poder devolver ese resultado a quien llamo la funcion
'''
def di_hola():
    return "hola" #bien puede ser un parametro o variable local
di_hola() # 'hola'
'''
También es posible devolver mas de una variable, separadas por ,. En el siguiente ejemplo tenemos una función que calcula la suma y media de tres números, y devuelve su resultado.
'''

def suma_y_media(a, b, c):
    suma = a+b+c
    media = suma/3
    return suma, media
suma, media = suma_y_media(9, 6, 3)
print(suma)  # 18
print(media) # 6.0