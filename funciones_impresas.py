import funciones_filtradoras as fnf
import funciones as fn
import funciones_str as fns


def cantidad_personajes(matriz:list[list])->None:
    """
    Cuenta la cantidad de filas de una matriz

    Args:
        matriz (list[list]): La matriz que ingrese el usuario

    returns:
        None: Imprime la cantidad de personajes
    """
    cantidad = fn.cantidad_elementos(matriz)
    mensaje = f"La cantidad de personajes dentro de nuestra matriz de datos es de: {cantidad} personajes cargados"
    print(mensaje)


def mostrar_razas_filtradas(matriz:list[list], categoria:str, tipo_raza:str, bandera:str)->None:
    """
    Imprime por pantalla la cantidad de personajes humanos o no.
    Args:
        matriz (list[list]): La matriz de datos
        bandera (str): El dato que indicara si queres filtrar humanos o no [humanos / no_humanos].
        tipo_raza(str): El tipo de raza el cual se filtrara
    Returns:
        None: Imprime la cantidad de personajes dentro de la matriz de datos.
    """
    matriz_filtrada = fnf.filtrar_matriz(matriz, categoria, tipo_raza, bandera)
    cantidad = fn.cantidad_elementos(matriz_filtrada)
    mensaje = f"La matriz filtrada con datos {bandera} a {tipo_raza} es de {cantidad} de datos cargados"
    print(mensaje)


def imprimir_datos(matriz:list[list], indice_col:int)->None:
    """
    Imprime los datos obtenidos de una matriz

    Args:
        matriz (list[list]): La matriz de datos
        indice_col (int): El indice de columna de la matriz de datos

    returns:
    None: Imprime por pantalla los datos obtenidos
    """
    mensaje = " "
    cantidad_filas = len(matriz)

    for indice_fila in range(cantidad_filas):
        valor_actual = matriz[indice_fila][indice_col]
        if indice_fila < 4:
            dato_truncado = fns.truncar_caracter(valor_actual)
        else:
            dato_truncado = valor_actual

        mensaje = f"{mensaje}{dato_truncado}"

        if indice_fila < cantidad_filas -1:
            mensaje = f"{mensaje}, "
    print(mensaje)

def imprimir_matriz_cxf(matriz:list[list])->None:
    """
    Recorre la matriz columna x fila

    :params: matriz(list[list]) = La matriz que ingrese el usuario

    :returns:
    None: Imprime por pantalla la matriz
    """

    cantidad_columnas = len(matriz[0])

    print(f"Nombre, Alias, Raza, Genero, Poder, Inteligencia, Velocidad \n")

    for indice_columna in range(cantidad_columnas):
        imprimir_datos(matriz, indice_columna)


def cantidad_personajes_filtrados(lista:list,categoria:str, criterio:str)->None:
    """
    Imprime la cantidad de personajes en una lista

    Args:
        lista (list): Una lista de datos ingresada por el usuario
        categoria (str): La categoria de los datos
        criterio (str): El criterio por el cual se filtro

    Returns:
        None: Imprime la cantidad de elementos de la lista
    """

    cantidad_elementos = len(lista)

    mensaje = f"La cantidad de personajes con {criterio} {categoria} es de {cantidad_elementos}\n"
    print(mensaje)



def imprimir_promedio_android(matriz:list[list])->None:
    """
    Imprime el promedio de inteligencia y poder de andorides

    Args:
        None:  Imprime el promedio de inteligencia y fuerza
    """

    matriz_androides = fnf.filtrar_matriz(matriz, "razas", "Android", "igual")
    promedio_inteligencia = fn.buscar_promedio(matriz_androides, "inteligencias")
    promedio_poder = fn.buscar_promedio(matriz_androides, "poderes")

    mensaje = f"El promedio de inteligencia es: {promedio_inteligencia}\n"
    mensaje = f"{mensaje} El promedio de poder es: {promedio_poder}"

    print(mensaje)

    