def verificar_matriz_vacia(matriz:list[list])->bool:
    """
    Verifica si la matriz es vacia

    :params: matriz(list[list]) = La matriz que ingrese le usuario

    :returns:
    Devuelve si la matriz es vacia
    """

    return len(matriz) == 0

def validar_rango_menu(numero_a:int, numero_b:int)->int:
    """
    Valida el valor que ingresa el usuario

    :params: numero_a = Numero desde donde comienza el rango
    :params: numero_b = Numero desde donde termina el rango

    :retruns:
    Devuelve el numero valido del usuario
    """

    numero_str = input(f"Ingrese una de las opciones nuestro menu: ")
    numero_int = int(numero_str)

    if not(numero_a <= numero_int <= numero_b):
        print("ERROR: El valor ingresado esta fuera de rango. Intentelo de nuevo")
        return validar_rango_menu(numero_a, numero_b)
    
    return numero_int

def validar_datos(dato_ingresado)->str:
    """
    Valida el nombre ingresado por el usuario

    Returns:
        str: El nombre valido ingresado por el usuario
    """

    mensaje =\
    """ERROR: El nombre ingresado no esta permitido en nuesta base de datos.
        Intentelo SIN caracteres especiales"""
    
    cadena_a_verificar = dato_ingresado
    cadena_a_verificar = cadena_a_verificar.replace(" ", "")
    cadena_a_verificar = cadena_a_verificar.replace("-", "")
    cadena_a_verificar = cadena_a_verificar.replace("(", "")
    cadena_a_verificar = cadena_a_verificar.replace(")", "")
    cadena_a_verificar = cadena_a_verificar.replace("/", "")
    

    if not(cadena_a_verificar.isalnum()):
        print(mensaje)
        dato_str = input("Ingrese nuevamente el dato: ")
        return validar_datos(dato_str)
    
    return dato_ingresado.title()

def validar_rango(dato_ingresado:str, numero_a:int, numero_b:int)->int:
    """
    Valida el valor que ingresa el usuario

    :params: numero_a = Numero desde donde comienza el rango
    :params: numero_b = Numero desde donde termina el rango

    :retruns:
    Devuelve el numero valido del usuario
    """

    dato_int = int(dato_ingresado)

    if not(numero_a <= dato_int <= numero_b):
        print("ERROR: El valor ingresado esta fuera de rango. Intentelo de nuevo")
        dato_str = input("Ingrese nuevamente el dato: ")
        return validar_rango(dato_str, numero_a, numero_b)
    
    return dato_int