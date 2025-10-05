import funciones_impresas as fni
import funciones as fn


def obtener_datos_filtrados(matriz:list[list], matriz_filtrada:list[list], indice_col:int)->list[list]:
    """
    Obtiene los datos filtrados de una matriz

    Args:
        matriz (list[list]): La matriz que ingrese el usuario
        matriz_filtrada (list[list]): La matriz auxiliar que retorna
        indice_col (int): El indice de columna

    Returns:
        list[list]: Devuelve la matriz filtrada
    """
    cantidad_filas = len(matriz)

    for indice_fila in range(cantidad_filas):
        dato = matriz[indice_fila][indice_col]
        matriz_filtrada[indice_fila].append(dato)
    return matriz_filtrada


def filtrar_matriz(matriz:list[list], categoria:str, tipo:str, bandera:str)->list[list]:
    """
    Filtra una matriz en base a una categoria dada por el usuario

    Args:
        matriz (list[list]): La matrizx que ingrese el usuario
        categoria (str): El campo de un indice dentro de la matriz dada
        tipo (str): El tipo de dato el cual se filtrara
        bandera (str): La manera es la que se filtrara la matriz [igual - distinto]

    Returns:
        list[list]: Devuelve una matriz filtrada
    """

    matriz_filtrada = [
        [],[],[],[],[],[],[]
    ]

    indice_a_filtrar = fn.mapear_indice(categoria)
    cantidad_columnas = len(matriz[indice_a_filtrar])

    for indice_columna in range(cantidad_columnas):
        valor_actual = matriz[indice_a_filtrar][indice_columna]
        if (bandera == "igual" and tipo in valor_actual) or\
            (bandera == "distinto" and not(tipo in valor_actual)):
            obtener_datos_filtrados(matriz, matriz_filtrada, indice_columna)

    return matriz_filtrada



def buscar_indices_por_criterio(matriz:list[list], categoria:str, criterio:str)->list:
    """
    Busca todos los indices en donde se cumplan los criterios en la categoria dada

    Args:
        matriz (list[list]): La matriz de datos
        categoria (str): La categoria de la matriz
        criterio (str): El criterio a filtrar

    Returns:
        list: Devuelve una lista de indices
    """

    indice_a_filtrar = fn.mapear_indice(categoria)
    cantidad_columnas = len(matriz[indice_a_filtrar])
    seleccionados = []
    destacado = None

    for indice_columna in range(cantidad_columnas):
        valor_actual = matriz [indice_a_filtrar] [indice_columna]
        if(destacado == None or (criterio == "mas" and destacado < valor_actual)) or\
            (destacado == None or (criterio == "menos" and destacado > valor_actual)):
            destacado = valor_actual
            seleccionados = [indice_columna]
        elif destacado == valor_actual:
            seleccionados.append(indice_columna)

    return seleccionados


def filtrar_matriz_por_criterio(matriz:list[list], categoria:str, criterio:str)->list[list]:
    """
    Filtra una matriz por el criterio en la categoria de la matriz de datos

    Args:
        matriz (list[list]): La matriz de datos
        categoria (str): La categoria de la matriz
        criterio (str): El criterio a filtrar

    Returns:
        list[list]: Devuelve una lista con el/los que cumplan el criterio en la categoria de la matriz
    """

    matriz_filtrada = [ [], [], [], [], [], [], [] ]

    indices_seleccionados = buscar_indices_por_criterio(matriz, categoria, criterio)
    cantidad_indices = len(indices_seleccionados)
    for indice in range(cantidad_indices):
        matriz_filtrada = obtener_datos_filtrados(matriz, matriz_filtrada, indices_seleccionados[indice])
            
    fni.cantidad_personajes_filtrados(indices_seleccionados, categoria, criterio)
    return matriz_filtrada

def buscar_indices_por_promedio(matriz:list[list], categoria:str, supera_promedio:str, promedio:float)->list:
    """
    Busca y guarda los indices que cumple con la condicion

    Args:
        matriz (list[list]): La matriz de datos
        categoria (str): La categoria de la matriz
        supera_promedio (str): El criterio a filtrar

    Returns:
        list: Devuelve una lista con los indices filtrados
    """

    seccion = fn.mapear_indice(categoria)
    cantidad_columnas = len(matriz[seccion])
    seleccionados = []

    for indice_columna in range(cantidad_columnas):
        valor_actual = matriz [seccion] [indice_columna]

        if(supera_promedio == "si" and  valor_actual > promedio) or\
            (supera_promedio == "no" and valor_actual < promedio):
            seleccionados.append(indice_columna)


    return seleccionados


def filtrar_matriz_por_promedio(matriz:list[list], categoria:str, supera_promedio:str)->list[list]:
    """
    Filtra una matriz por un promedio determinado

    Args:
        matriz (list[list]): La matriz de datos
        categoria (str): La categoria de la matriz
        supera_promedio (str): El criterio a filtrar

    Returns:
        list[list]: Devuelve una matriz filtrada
    """

    matriz_filtrada = [ [], [], [], [], [], [], [] ]


    promedio =fn.buscar_promedio(matriz, categoria)
    indices_promedios = buscar_indices_por_promedio(matriz, categoria, supera_promedio, promedio)
    cantidad_indices = len(indices_promedios)
    for indice in range(cantidad_indices):
        matriz_filtrada = obtener_datos_filtrados(matriz, matriz_filtrada, indices_promedios[indice])
            

    return matriz_filtrada


def filtrar_debiles_a_saiyans(matriz:list[list])->list[list]:
    """
    Filtra los personajes mas debiles que el poder de los de raza Saiyan

    Args:
        matriz (list[list]): La matriz de datos


    Returns:
        list[list]: Devuelve la matriz con personajes mas debiles a la raza Saiyan
    """

    matriz_filtrada = [[],[],[],[],[],[],[]]
    indice_a_filtrar = fn.mapear_indice("poderes")

    matriz_saiyans = filtrar_matriz(matriz, "razas", "Saiyan", "igual")
    indices_saiyans_debiles = buscar_indices_por_criterio(matriz_saiyans, "poderes", "menos")
    indice_poder_saiyan = indices_saiyans_debiles[0]
    poder_saiyan = matriz[indice_a_filtrar] [indice_poder_saiyan]

    matriz_sin_saiyans = filtrar_matriz(matriz, "razas", "Saiyan", "distinto")
    cantidad_columnas = len(matriz_sin_saiyans[indice_a_filtrar])

    for indice_columna in range(cantidad_columnas):
        poder_actual = matriz_sin_saiyans[indice_a_filtrar][indice_columna]

        if poder_actual < poder_saiyan:
            matriz_filtrada = obtener_datos_filtrados(matriz_sin_saiyans, matriz_filtrada, indice_columna)
    return matriz_filtrada



def filtrar_mayorigual_a_kryptonian(matriz:list[list])->list[list]:
    """
    Filtra la matriz con los personaje NO Kryptonian que iguales o superen el promedio poder de la raza kryptonian

    Args:
        matriz (list[list]): La matriz de datos

    Returns:
        list[list]: Devuelve la amtriz filtrada
    """

    matriz_filtrada = [[],[],[],[],[],[],[]]
    matriz_kryptonian = filtrar_matriz(matriz, "razas", "Kryptonian", "igual")
    promedio_poder_kryptonian = fn.buscar_promedio(matriz_kryptonian, "poderes")

    matriz_no_kryptonian = filtrar_matriz(matriz, "razas", "Kryptonian", "distinto")
    indice_filtrar = fn.mapear_indice("poderes")
    
    for indice_columna in range(len(matriz_no_kryptonian[indice_filtrar])):
        poder_actual = matriz_no_kryptonian[indice_filtrar][indice_columna]
        if poder_actual >= promedio_poder_kryptonian:
            matriz_filtrada = obtener_datos_filtrados(matriz_no_kryptonian, matriz_filtrada, indice_columna)
    return matriz_filtrada



def filtrar_debajo_stats_saiyans(matriz:list[list])->list[list]:
    """
    Filtra la matriz de datos

    Args:
        matriz (list[list]): La matriz de datos

    Returns:
        list[list]: Devuelve una matriz con solo los personajes que estan debajo de la raza Saiyan
    """

    matriz_filtrada = [[],[],[],[],[],[],[]]

    matriz_saiyan = filtrar_matriz(matriz, "razas", "Saiyan", "igual")
    promedio_stats = fn.obtener_promedio_stats(matriz_saiyan)

    matriz_sin_saiyan = filtrar_matriz(matriz, "razas", "Saiyan", "distinto")
    indice_poder = fn.mapear_indice("poderes")

    cantidad_columnas = len(matriz_sin_saiyan[0])

    for indice_columna in range(cantidad_columnas):
        poder_actual = matriz_sin_saiyan[indice_poder][indice_columna]
        inteligencia_actual = matriz_sin_saiyan[indice_poder+1][indice_columna]
        velocidad_actual = matriz_sin_saiyan[indice_poder+2][indice_columna]

        if poder_actual < promedio_stats and\
        inteligencia_actual < promedio_stats and\
        velocidad_actual < promedio_stats:
            obtener_datos_filtrados(matriz_sin_saiyan, matriz_filtrada, indice_columna)
    return(matriz_filtrada)
