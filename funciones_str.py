


def truncar_caracter(dato_cargado:str)->str:
    """
    Acortar los datos solo si es necesario

    Args:
        dato_cargado (str): El dato de la matriz de datos

    Returns:
        str: Devuelve el dato acortado solo si es necesario (15 caracteres como máximo)
    """

    nuevo_dato =""
    limite = 1

    if len(dato_cargado) > 15:
        
        for indice_str in range(len(dato_cargado)):
            nuevo_dato += dato_cargado[indice_str]

            if limite == 15:
                break
            limite +=1
        return nuevo_dato
    else:
        return dato_cargado
