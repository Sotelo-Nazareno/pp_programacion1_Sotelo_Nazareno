import funciones as fn
import funciones_filtradoras as fnf


def ordenar_matriz(matriz:list[list], categoria:str, modo:str)->list[list]:
    """
    Ordena la matriz

    :params: matriz(list[list]) = La matriz que ingrese el usuario
    :params: categoria(str) = La lista por la cual se ordenara la matriz
    :params: modo(str) = El orden de la matriz

    :returns:
    Devuelve la matriz ordenada
    """
    indice_ordenar = fn.mapear_indice(categoria)

    for indice_columna in range(len(matriz[indice_ordenar])-1):
        indice_seleccionado = indice_columna

        for sig_indice_columna in range(indice_columna +1, len(matriz[indice_ordenar]), 1):
            if ( modo == "ASC" and matriz[indice_ordenar] [indice_seleccionado] > matriz [indice_ordenar] [sig_indice_columna] or\
                modo == "DES" and matriz[indice_ordenar] [indice_seleccionado] < matriz [indice_ordenar] [sig_indice_columna]):
                indice_seleccionado = sig_indice_columna

            if indice_seleccionado != indice_columna:
                auxiliar = matriz [indice_ordenar] [indice_seleccionado]
                matriz [indice_ordenar] [indice_seleccionado] = matriz[indice_ordenar][indice_columna] 
                matriz[indice_ordenar][indice_columna] = auxiliar

    return matriz


def concatenar_matrices(matriz_vacia:list[list], matriz:list[list])->list[list]:
    """
    Concatena dos matrices

    Args:
        matriz_vacia (list[list]): La matriz vacia
        matriz (list[list]): La matriz de datos

    Returns:
        list[list]: Devuelve la matriz concatenada
    """

    for indice_fila in range(len(matriz_vacia)):
        fila_concatenada = matriz_vacia[indice_fila] + matriz[indice_fila]
        matriz_vacia[indice_fila] = fila_concatenada


def ordenar_personalizado(matriz:list[list])->list[list]:
    """
    Ordena la matriz de datos

    Args:
        matriz (list[list]): La matriz de datos

    Returns:
        list[list]: Devuelve la matriz de datos ordenada por grupos de raza, las razas por poder y  alfabeticamente en la matriz
    """
    matriz_ordenada = [[],[],[],[],[],[],[]]
    cantidad_razas = 16

    for razas in range(cantidad_razas):
        matriz_raza = fnf.filtrar_matriz(matriz, "razas", fn.mapear_razas(razas), "igual")
        matriz_raza_ordenada = ordenar_matriz(matriz_raza, "poderes", "DES")
        concatenar_matrices(matriz_ordenada, matriz_raza_ordenada)

    return matriz_ordenada