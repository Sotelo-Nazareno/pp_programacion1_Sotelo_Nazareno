import funciones as fn
import funciones_impresas as fni
import funciones_filtradoras as fnf
import funciones_ordenadoras as fno
import validaciones as vl
import os




def menu_opciones(lista_nombres:list, lista_alias:list, lista_razas:list, lista_generos:list, lista_poderes:list, lista_inteligencias:list, lista_velocidades:list)->None:
    """
    Imprime un menu de opciones

    Args:
        lista_nombres (list): Lista de nombres
        lista_alias (list): Lista de alias
        lista_razas (list): Lista de razas
        lista_generos (list): Lista de generos
        lista_poderes (list): Lista de poderes
        lista_inteligencias (list): Lista de inteligencias
        lista_velocidades (list): Lista de velocidades
    
    Returns:
        None: No devuelve nada, ya que se imprime por terminal
    """

    corriendo = True
    matriz_datos = []
    mensaje_error = f"ERROR: Debe crear una matriz de datos(opcion[1]) antes de acceder a esta opcion"
    mensaje_matriz_cargada = f"Felicidades, tu matriz de datos se cargo con exito!"
    print("Bienvenido!")

    opciones =\
        """
            [1] Crear Matriz
            [2] Agregar personaje 
            [3] Cantidad de existencias
            [4] Existencias personajes Human
            [5] Existencias personajes que no sean Human
            [6] Mostrar en Detalle
            [7] Mostrar Saiyans
            [8] Mostrar más poderoso
            [9] Mostrar más inteligente
            [10] Filtrar Menor velocidad
            [11] Filtrar Personajes Débiles A Raza Saiyan
            [12] Filtrar No-Binario Mas Veloces
            [13] Calcular el promedio de inteligencia y poder de los personajes que sean de raza Android.
            [14] Mostar info personajes que NO sean Kryptonian y superen o igualen el promedio de poder de personajes de raza Kryptonian.
            [15] Mostrar info de los personajes no Saiyan cuyos stats estén por debajo del índice de ataque Saiyan, obtenido de la ecuación (promedio poder + promedio inteligencia + promedio velocidad) / 3.
            [16] Ordenar por Más Inteligente orden DES
            [17] Ordenar por Menos Inteligente orden ASC [not Human]
            [18] Ordenar por Más Poder orden DES [not Human]
            [19] Ordenar por Más Velocidad ASC
            [20] Ordenar personalizado
            [21] Trasponer la matriz y mostrar su información prolija por Raza ASC.
            [22] Salir
        """

    while corriendo:

        print(opciones)
        
        seleccion = vl.validar_rango_menu(vl.validar_numero_menu(),1, 22)

        match seleccion:
            case 1:
                matriz_datos = fn.crear_matriz(lista_nombres, lista_alias, lista_razas, lista_generos, lista_poderes, lista_inteligencias, lista_velocidades)
                print(matriz_datos)
                print(mensaje_matriz_cargada)
            case 2:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fn.agregar_personaje(matriz_datos)
                else:
                    print(mensaje_error)
            case 3:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.cantidad_personajes(matriz_datos)
                else:
                    print(mensaje_error)
            case 4:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.mostrar_razas_filtradas(matriz_datos, "razas", "Human", "igual")
                    fni.imprimir_matriz_cxf(fnf.filtrar_matriz(matriz_datos, "razas", "Human", "igual"))
                else:
                    print(mensaje_error)
            case 5:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.mostrar_razas_filtradas(matriz_datos, "razas", "Human", "distinto")
                    fni.imprimir_matriz_cxf(fnf.filtrar_matriz(matriz_datos, "razas", "Human", "distinto"))
                else:
                    print(mensaje_error)
            case 6:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.imprimir_matriz_cxf(matriz_datos)
                else:
                    print(mensaje_error)
            case 7:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.imprimir_matriz_cxf(fnf.filtrar_matriz(matriz_datos, "razas", "Saiyan", "igual"))
                else:
                    print(mensaje_error)
            case 8:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.imprimir_matriz_cxf(fnf.filtrar_matriz_por_criterio(matriz_datos, "poderes", "mas"))
                else:
                    print(mensaje_error)
            case 9:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.imprimir_matriz_cxf(fnf.filtrar_matriz_por_criterio(matriz_datos, "inteligencias", "mas"))
                else:
                    print(mensaje_error)
            case 10:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.imprimir_matriz_cxf(fnf.filtrar_matriz_por_promedio(matriz_datos, "velocidades", "no"))
                else:
                    print(mensaje_error)
            case 11:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.imprimir_matriz_cxf(fnf.filtrar_debiles_a_saiyans(matriz_datos))
                else:
                    print(mensaje_error)
            case 12:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    matriz_no_binarios = fnf.filtrar_matriz(matriz_datos, "generos", "No-Binario", "igual")
                    fni.imprimir_matriz_cxf(fnf.filtrar_matriz_por_criterio(matriz_no_binarios, "velocidades", "mas"))
                else:
                    print(mensaje_error)
            case 13:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    matriz_android = fnf.filtrar_matriz(matriz_datos, "razas", "Android", "igual")
                    fni.imprimir_promedio_android(matriz_datos)
                    fni.imprimir_matriz_cxf(matriz_android)
                else:
                    print(mensaje_error)
            case 14:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.imprimir_matriz_cxf(fnf.filtrar_mayorigual_a_kryptonian(matriz_datos))
                else:
                    print(mensaje_error)
            case 15:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.imprimir_matriz_cxf(fnf.filtrar_debajo_stats_saiyans(matriz_datos))
                    promedio_stats = fn.obtener_promedio_stats(fnf.filtrar_matriz(matriz_datos, "razas", "Saiyan", "igual"))
                    print(promedio_stats)
                else:
                    print(mensaje_error)
            case 16:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.imprimir_matriz_cxf(fno.ordenar_matriz(matriz_datos, "inteligencias", "DES"))
                else:
                    print(mensaje_error)
            case 17:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    matriz_no_human = fnf.filtrar_matriz(matriz_datos, "razas", "Human", "distinto")
                    fni.imprimir_matriz_cxf(fno.ordenar_matriz(matriz_no_human, "inteligencias", "ASC"))
                else:
                    print(mensaje_error)
            case 18:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    matriz_no_human = fnf.filtrar_matriz(matriz_datos, "razas", "Human", "distinto")
                    fni.imprimir_matriz_cxf(fno.ordenar_matriz(matriz_no_human, "poderes", "DES"))
                else:
                    print(mensaje_error)
            case 19:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.imprimir_matriz_cxf(fno.ordenar_matriz(matriz_datos, "velocidades", "ASC"))
                else:
                    print(mensaje_error)
            case 20:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.imprimir_matriz_cxf(fno.ordenar_personalizado(matriz_datos))
                else:
                    print(mensaje_error)
            case 21:
                if not(vl.verificar_matriz_vacia(matriz_datos)):
                    fni.imprimir_matriz_cxf_prolijo(fno.ordenar_matriz(matriz_datos, "razas", "ASC"))
                else:
                    print(mensaje_error)
            case 22:
                print("Hasta Luego!")
                corriendo = False

        os.system('pause')
        os.system('cls')