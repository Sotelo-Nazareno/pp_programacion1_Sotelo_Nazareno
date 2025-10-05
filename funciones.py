import validaciones as vl


def crear_matriz(lista_a:list, lista_b:list, lista_c:list, lista_d:list, lista_e:list, lista_f:list, lista_g:list)->list[list]:
    """
    Crea una matriz

    Args:
        lista_a (list): La lista que ingrese el usuario
        lista_b (list): La lista que ingrese el usuario
        lista_c (list): La lista que ingrese el usuario
        lista_d (list): La lista que ingrese el usuario
        lista_e (list): La lista que ingrese el usuario
        lista_f (list): La lista que ingrese el usuario
        lista_g (list): La lista que ingrese el usuario

    Returns:
        list[list]: Devuelve una matriz con las listas asignadas
    """

    mi_matriz = [
        lista_a,
        lista_b,
        lista_c,
        lista_d,
        lista_e,
        lista_f,
        lista_g
    ]

    return mi_matriz


def cantidad_elementos(matriz:list[list])->int:
    """
    Cuenta la cantidad de elementos de una matriz

    :params: matriz(list[list]) = La matriz que ingrese el usuario

    :returns:
    Devuelve la cantidad total de elementos de la matriz
    """

    return(len(matriz[0]))



def campo_por_indice(indice:int)->str:
    """
    Devuelve el campo de un indice dado

    Args:
        indice (int): El indice de la lista

    Returns:
        str: Devuelve el campo de ese indice dado
    """
    match indice:
        case 0:
            return "nombre"
        case 1:
            return "alias"
        case 2:
            return "raza"
        case 3:
            return "genero"
        case 4:
            return "poder"
        case 5:
            return "inteligencia"
        case 6:
            return "velocidad"

def guardar_dato(matriz:list[list])->list:
    """
    Guarda un nuevo dato a una lista

    Args:
        matriz (list[list]): La matriz que ingrese el usuario

    Returns:
        [list]: Devuelve una lista con el nuevo dato ingresado
    """

    lista_personaje = []
    cantidad_datos = len(matriz)


    for indice_dato in range(cantidad_datos):
        campo = campo_por_indice(indice_dato)
        nuevo_dato = input(f"Carge un/a {campo} en la matriz de datos: ")

        if indice_dato < 4:
            nuevo_dato = vl.validar_datos(nuevo_dato, indice_dato)
        else:
            numero_validado = vl.validar_numero(nuevo_dato, indice_dato)
            nuevo_dato = vl.validar_rango(numero_validado, 0,100)




        lista_personaje.append(nuevo_dato)

    return lista_personaje


def agregar_personaje(matriz:list[list])->list[list]:
    """
    Agrega un nuevo dato a la matriz de datos

    Args:
        matriz (list[list]): La matriz de datos ingresada por el usuario

    Returns:
        list[list]: La matriz de datos con el nuevo dato
    """

    cantidad_filas = len(matriz)
    nuevo_dato = guardar_dato(matriz)

    for indice_campo in range(cantidad_filas):
        matriz[indice_campo].append(nuevo_dato[indice_campo])
    
    return matriz


def mapear_indice(seccion:str)->int:
    """
    Deriva una de las secciones (nombre, vistas, duracion) del video por un indice

    :params: seccion(str) = La seccion que ingresara el usuario 

    :returs:
    Devuelve el numero de indice
    """

    match seccion:
        case "nombres":
            return 0
        case "alias":
            return 1
        case "razas":
            return 2
        case "generos":
            return 3
        case "poderes":
            return 4
        case "inteligencias":
            return 5
        case "velocidades":
            return 6
        


def buscar_promedio(matriz:list[list], categoria:str)->float:
    """
    Calcula el promedio de la suma de los elementos de la lista fila

    :params: matriz(list[list]) = La matriz que ingrese le usuario
    :params: fila(str) = La fila matriz a la que se quiere promediar (nombre, vistas, duracion)

    :returns:
    Devuelve el promedio de toda la fila asignada
    """

    indice_a_promediar = mapear_indice(categoria)
    cantidad_elementos = len(matriz[indice_a_promediar])
    sumatoria = 0

    for indice_columna in range(cantidad_elementos):
        valor_actual = matriz[indice_a_promediar][indice_columna]
        sumatoria += valor_actual

    if sumatoria > 0:
        promedio = sumatoria / cantidad_elementos
    else:
        promedio = 0

    return(promedio)



def obtener_promedio_stats(matriz:list[list])->float:
    """
    Obtiene el promedio de los stats de poder de una matriz determinada, los stats de poder son (promedio poder + promedio inteligencia + promedio velocidad) / 3. )

    Args:
        matriz (list[list]): La matriz de datos

    Returns:
        float: Devuelve el promedio de los stats de poder de toda la matriz
    """

    promedio_poder = buscar_promedio(matriz, "poderes")
    promedio_inteligencia = buscar_promedio(matriz, "inteligencias")
    promedio_velocidad = buscar_promedio(matriz, "velocidades")

    promedio_total = promedio_poder + promedio_inteligencia + promedio_velocidad

    return(promedio_total / 3)


def mapear_razas(indice:int)->str:
    """
    Mapea las razas por un numero

    Args:
        indice (int): El numero representrado por una raza

    Returns:
        str: Devuelve la raza representada por un numero
    """

    match indice:
        case 0:
            return "Alpha"
        case 1:
            return "Android"
        case 2:
            return "Animal"
        case 3:
            return "Asgardian"
        case 4:
            return "Czarnian"
        case 5:
            return "Demi-God"
        case 6:
            return "Demon"
        case 7:
            return "Desconocido"
        case 8:
            return "Eternal"
        case 9:
            return "Human"
        case 10:
            return "Inhuman"
        case 11:
            return "Kryptonian"
        case 12:
            return "Mutant"
        case 13:
            return "New God"
        case 14:
            return "Saiyan"
        case 15:
            return "Vampire"
