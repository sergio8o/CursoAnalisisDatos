'''
    Un entorno virtual en Python, es un entorno parcialmente aislado, que permite instalar paquetes
    para que los use una aplicacion en particular en lugar de usarlos en todo el sistema.
    Permiten aislar la configuracion de un proyecto, indpendientemente de otros proyectos Python
    AISLA PROYECTOS, QUE NECESITAN VERSIONES DISTINTAS DE LIBRERIAS
    SCRIPTs: SON ARCHIVOS CODIGO FUENTE
    Ciertas librerias elegidas por mi , se instalan en un entorno virtual
    Para un script 1, y en otros entornos se usan las mismas y/o otras librerias
    o algunas de las mismas. Lo que pasara es que los scripts que les falte librerias no se podroan
    ejecutar en ese entorno aunque en el que pertenecen si.
    Porque las librerias no se instalan en el sistema , solo en el entorno.
    No esta de acceso global
    Tambien sirve para tener proyectos con diferentes versiones de una misma biblioteca.
    Pycharm crea entornos virtuales para gestionar cada proyecto
    Nos dan dos ubicaciones una donde se guardara el proyecto y otra donde se creara el entorno virtual
    Los entornos de python se crean a partir de la version de python existente en mi pc



    NOTA:
    PARA EJECUTAR UN SCRIPT, se busca en los directorios la carpeta donde se encuentra
    el script a ejectuar y con la variable de entorno python: python
    lo ejecuto
    python archivo.py
    Si mi script necesita o importa librerias que no estan instaladas en el sistema puede hacerlo con
    el instalador de paquetes de python pip
    pip --version , para verificar que lo tengo instalado, se instala con python
    Voy al buscador y coloco : pip nombre_libreria, copio el comando y lo pego en el cmd
    A veces junto con una libreria, se instalan otras complementarias
'''