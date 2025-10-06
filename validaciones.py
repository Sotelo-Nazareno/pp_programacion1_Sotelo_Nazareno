import funciones as fn


def verificar_matriz_vacia(matriz:list[list])->bool:
    """
    Verifica si la matriz es vacia

    :params: matriz(list[list]) = La matriz que ingrese le usuario

    :returns:
    Devuelve si la matriz es vacia
    """

    return len(matriz) == 0


def validar_numero_menu()->int:
    """
    Valida si un dato es un numero

    Args:
        dato_ingresado (str): Dato ingresado por el usuario

    Returns:
        int: Devuelve un numero validado
    """
    dato_ingresado = input(f"Ingrese una de las opciones nuestro menu: ")
    mensaje_error = f"ERROR: El dato ingresado debe ser un numero: "
    if not(dato_ingresado.isdigit()):
        print(mensaje_error)
        return validar_numero_menu()
    
    return dato_ingresado

def validar_rango_menu(numero_str:str, numero_a:int, numero_b:int)->int:
    """
    Valida el valor que ingresa el usuario

    :retruns:
    Devuelve el numero valido del usuario

    Args:
        numero_str (str): El numero ingresado a validar
        numero_a (int): Numero desde donde comienza el rango
        numero_b (int): Numero desde donde termina el rango

    Returns:
        int: Devuelve un numero validado
    """

    numero_int = int(numero_str)

    if not(numero_a <= numero_int <= numero_b):
        print(f"ERROR: El valor ingresado esta fuera de rango. Intentelo de nuevo con un valor entre [{numero_a} - {numero_b}]")
        numero_str = input(f"Ingrese una de las opciones nuestro menu: ")
        return validar_rango_menu(numero_str, numero_a, numero_b)
    
    return numero_int

def pertenece_raza(dato_ingresado:str)->bool:
    """
    Valida si el dato ingresado pertenece a las razas cargadas

    Args:
        dato_ingresado(str): El dato a validar del usuario

    Returns:
        bool: Devuelve el valor del dato ingresado
    """

    return(dato_ingresado == "Alpha" or
        dato_ingresado == "Android" or
        dato_ingresado == "Animal" or
        dato_ingresado == "Asgardian" or
        dato_ingresado == "Czarnian" or
        dato_ingresado == "Demi-God" or
        dato_ingresado == "Demon" or
        dato_ingresado == "Desconocido" or
        dato_ingresado == "Eternal" or
        dato_ingresado == "Human" or
        dato_ingresado == "Inhuman" or
        dato_ingresado == "Kryptonian" or
        dato_ingresado == "Mutant" or
        dato_ingresado == "New God" or
        dato_ingresado == "Saiyan" or
        dato_ingresado == "Vampire")

def validar_raza(dato_ingresado:str)->str:
    """
    Valida si la raza ingresada pertence a la base de datos

    Args:
        dato_ingresado (str): El dato ingresado a validar

    Returns:
        str: Devuevle el dato validado
    """
    dato_ingresado = dato_ingresado.title()
    mensaje_error = f"La raza ingresada no esta cargada en nuesta bases de datos. Por favor intenetelo de nuevo"
    if not(pertenece_raza(dato_ingresado)):
        print(mensaje_error)
        dato_ingresado = input("Ingrese la raza del personaje: ")
        return(validar_raza(dato_ingresado))

    return dato_ingresado

def pertenece_genero(dato_ingresado:str)->bool:
    """
    Valida si el dato ingresado es valido

    Args:
        dato_ingresado (str): El dato ingresado por el usuario a validar

    Returns:
        bool: Devuelve si el dato es valido
    """

    return(dato_ingresado == "Masculino" or
        dato_ingresado == "No-Binario" or
        dato_ingresado == "Femenino")



def validar_genero(dato_ingresado:str)->str:
    """
    Valida si la raza ingresada pertence a la base de datos

    Args:
        dato_ingresado (str): El dato ingresado a validar

    Returns:
        str: Devuevle el dato validado
    """
    dato_ingresado = dato_ingresado.title()
    mensaje_error = f"El genero ingresado no esta cargada en nuesta bases de datos. Por favor intenetelo de nuevo"
    if not(pertenece_genero(dato_ingresado)):
        print(mensaje_error)
        dato_ingresado = input("Ingrese el genero del personaje: ")
        return(validar_genero(dato_ingresado))

    return dato_ingresado

def reemplazar_caracter(palabra:str, caracter_a_cambiar:str, caracter_nuevo:str)->str:
    """
    Reemplaza un caracter de una cadena de strings

    Args:
        palabra (str): Cadena de strings
        caracter_a_cambiar (str): El caracter el cual sera reemplazado
        caracter_nuevo (str): El caracter por el cual se sustituye

    Returns:
        str: Devuelve la cadena de strings con los caracteres reemplazados
    """
    palabra_nueva = ""

    for indice_char in range(len(palabra)):
        char_actual = palabra[indice_char]
        if char_actual == caracter_a_cambiar:
            palabra_nueva += caracter_nuevo
        else:
            palabra_nueva += char_actual
    return(palabra_nueva)


def validar_datos(dato_ingresado, indice)->str:
    """
    Valida el nombre ingresado por el usuario

    Args:
        dato_ingresado(str) = El dato ingresado a validar
        indice(int) = El numero de indice

    Returns:
        str: El nombre valido ingresado por el usuario
    """

    mensaje =\
    """ERROR: El dato ingresado no esta permitido en nuesta base de datos.
        Intentelo devuelta SIN caracteres especiales y respetando nuesta sintaxis en cada seccion"""
    
    dato_a_verificar = dato_ingresado
    dato_a_verificar = reemplazar_caracter(dato_a_verificar, " ", "")
    dato_a_verificar = reemplazar_caracter(dato_a_verificar, "-", "")
    dato_a_verificar = reemplazar_caracter(dato_a_verificar, "(", "")
    dato_a_verificar = reemplazar_caracter(dato_a_verificar, ")", "")
    dato_a_verificar = reemplazar_caracter(dato_a_verificar, "/", "")
    categoria = fn.campo_por_indice(indice)
    

    if indice < 2:
        if not(dato_a_verificar.isalnum()):
            print(mensaje)
            dato_str = input(f"Ingrese nuevamente el dato {categoria}: ")
            return validar_datos(dato_str, indice)
    else:
        if not(dato_a_verificar.isalpha()):
            print(mensaje)
            dato_str = input(f"Ingrese nuevamente el dato {categoria}: ")
            return validar_datos(dato_str, indice)
        
        if indice == 2:
            dato_ingresado = validar_raza(dato_a_verificar)
        elif indice == 3:
            dato_ingresado =  validar_genero(dato_a_verificar)

    return dato_ingresado.title()

def validar_rango(dato_ingresado:str, numero_a:int, numero_b:int)->int:
    """
    Valida el valor que ingresa el usuario

    Args:
        dato_ingresado (str): El dato a validar
        numero_a (int): Numero desde donde comienza el rango
        numero_b (int): Numero desde donde termina el rango
    Returns:
        int: Devuelve el numero valido del usuario
    """

    dato_int = int(dato_ingresado)

    if not(numero_a <= dato_int <= numero_b):
        print("ERROR: El valor ingresado esta fuera de rango. Intentelo de nuevo")
        dato_str = input(f"Ingrese nuevamente el valor entre [{numero_a} - {numero_b}]: ")
        return validar_rango(dato_str, numero_a, numero_b)
    
    return dato_int

def validar_numero(dato_ingresado:str, indice:int)->int:
    """
    Valida si un dato es un numero

    Args:
        dato_ingresado (str): Dato ingresado por el usuario
        numero_a (int): Primer rango
        numero_b (int): Segundo rango

    Returns:
        int: Devuelve un numero validado
    """
    categoria = fn.campo_por_indice(indice)
    mensaje_error = f"ERROR: El dato ingresado debe ser un numero: "
    if not(dato_ingresado.isdigit()):
        print(mensaje_error)
        dato_str = input(f"Ingrese nuevamente el dato {categoria}: ")
        return validar_numero(dato_str, indice)
    
    return dato_ingresado