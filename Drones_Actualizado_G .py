drones_list = []
cola_misiones = []
grafo_zonas={}

def registrar_dron(codigo, modelo, velocidad, capacidad, bateria):

    dron = {
        "codigo": codigo,
        "modelo": modelo,
        "velocidad": velocidad,
        "capacidad": capacidad,
        "bateria": bateria,
        "estado": "Disponible"
    }

    drones_list.append(dron)



# cola fifo

def agregar_mision_a_cola(codigo, zona, tipo, prioridad, personas, distancia):

    mision = {
        "codigo": codigo,
        "zona": zona,
        "tipo": tipo,
        "prioridad": prioridad,
        "personas": personas,
        "distancia": distancia,
        "estado": "Pendiente"
    }

    cola_misiones.append(mision)

    actualizar_arbol_misiones()

    print(f"Mision {codigo} agregada al final de la cola.")



def atender_mision_de_cola():

    if len(cola_misiones) == 0:

        print("No hay misiones pendientes.")

        return None


    mision_atendida = cola_misiones.pop(0)

    mision_atendida["estado"] = "Atendida"

    print(
        f"Se atendio la mision: "
        f"{mision_atendida['codigo']} "
        f"de la zona {mision_atendida['zona']}"
    )

    return mision_atendida




# ordenar algoritmos


def ordenar_drones_por_bateria_insercion():

    arreglo = []

    for elemento in drones_list:

        arreglo.append(elemento)


    n = len(arreglo)


    for i in range(1, n):

        clave = arreglo[i]

        j = i - 1


        print(f"Insertando... Dron {clave['codigo']}")


        while j >= 0 and arreglo[j]["bateria"] > clave["bateria"]:


            print(f"  Moviendo... Dron {arreglo[j]['codigo']}")


            arreglo[j + 1] = arreglo[j]

            j = j - 1


        arreglo[j + 1] = clave


    return arreglo




def ordenar_margeSort(arreglo):

    if len(arreglo) <= 1:

        return arreglo


    medio = len(arreglo) // 2


    izquierda = []

    derecha = []


    for i in range(0, medio):

        izquierda.append(arreglo[i])


    for i in range(medio, len(arreglo)):

        derecha.append(arreglo[i])


    print(
        f"Dividiendo... Izq: {len(izquierda)} elementos | "
        f"Der: {len(derecha)} elementos"
    )


    izquierda = ordenar_margeSort(izquierda)

    derecha = ordenar_margeSort(derecha)



    resultado = []

    pos_izq = 0

    pos_der = 0


    print("Mezclando...")



    while pos_izq < len(izquierda) and pos_der < len(derecha):


        if izquierda[pos_izq]["velocidad"] <= derecha[pos_der]["velocidad"]:


            resultado.append(izquierda[pos_izq])

            pos_izq = pos_izq + 1


        else:

            resultado.append(derecha[pos_der])

            pos_der = pos_der + 1



    for i in range(pos_izq, len(izquierda)):

        resultado.append(izquierda[i])



    for i in range(pos_der, len(derecha)):

        resultado.append(derecha[i])



    print("Resultado:")


    for d in resultado:

        print(
            f"  {d['codigo']} -> "
            f"Velocidad: {d['velocidad']} km/h"
        )


    return resultado




def quickSort_distancia(arreglo):


    if len(arreglo) <= 1:

        return arreglo


    pivote = arreglo[-1]


    print(
        f"Pivote... {pivote['codigo']} "
        f"({pivote['distancia']} km)"
    )


    menores = []

    mayores = []


    for i in range(len(arreglo)-1):


        if arreglo[i]["distancia"] <= pivote["distancia"]:

            menores.append(arreglo[i])


        else:

            mayores.append(arreglo[i])



    print(
        f"Partición... Menores: {len(menores)} "
        f"| Mayores: {len(mayores)}"
    )



    izquierda = quickSort_distancia(menores)

    derecha = quickSort_distancia(mayores)



    resultado = izquierda + [pivote] + derecha



    print("Resultado:")


    for d in resultado:

        print(
            f"  {d['codigo']} -> "
            f"Distancia: {d['distancia']} km"
        )


    return resultado




# ORDENAMIENTO BURBUJA POR PRIORIDAD

def burbuja_prioridad(arreglo):


    lista = []


    for elemento in arreglo:

        lista.append(elemento)



    n = len(lista)



    for i in range(n-1):


        for j in range(n-i-1):


            print(
                f"Comparando {lista[j]['codigo']} "
                f"con {lista[j+1]['codigo']}"
            )



            if lista[j]["prioridad"] > lista[j+1]["prioridad"]:



                print(
                    f"Intercambiando {lista[j]['codigo']} "
                    f"con {lista[j+1]['codigo']}"
                )



                auxiliar = lista[j]

                lista[j] = lista[j+1]

                lista[j+1] = auxiliar



                print("Lista actual:")


                for m in lista:

                    print(
                        f"{m['codigo']} - "
                        f"Prioridad: {m['prioridad']}"
                    )



    return lista
# Buscar un dron disponible

def buscar_dron_disponible():

    print("\nBuscando dron disponible...")

    for dron in drones_list:

        if dron["estado"] == "Disponible":

            print(f"{dron['codigo']} disponible")

            print(f"\nDron asignado: {dron['codigo']}")

            dron["estado"] = "Ocupado"

            return dron

        else:

            print(f"{dron['codigo']} ocupado")


    print("No hay drones disponibles.")

    return None




# Mostrar la siguiente mision

def mostrar_siguiente_mision():

    if len(cola_misiones) == 0:

        print("No hay misiones pendientes.")

        return


    m = cola_misiones[0]


    print("Siguiente mision:")

    print(f"Codigo: {m['codigo']}")

    print(f"Zona: {m['zona']}")

    print(f"Tipo: {m['tipo']}")

    print(f"Prioridad: {m['prioridad']}")

    print(f"Personas afectadas: {m['personas']}")

    print(f"Distancia: {m['distancia']} km")

    print(f"Estado: {m['estado']}")




# BST

def insertar(raiz, codigo):

    if raiz is None:

        print(f"Insertado: {codigo}")

        return {
            "codigo": codigo,
            "izquierdo": None,
            "derecho": None
        }



    if codigo < raiz["codigo"]:

        raiz["izquierdo"] = insertar(
            raiz["izquierdo"],
            codigo
        )

    else:

        raiz["derecho"] = insertar(
            raiz["derecho"],
            codigo
        )


    return raiz



def buscar(raiz, codigo):

    actual = raiz


    while actual is not None:

        print(
            f"Visitando nodo... {actual['codigo']}"
        )


        if codigo == actual["codigo"]:

            print("Encontrado")

            return True



        if codigo < actual["codigo"]:

            actual = actual["izquierdo"]

        else:

            actual = actual["derecho"]



    print("No encontrado")

    return False




def preorden(raiz):

    if raiz is None:

        return


    print(raiz["codigo"])

    preorden(raiz["izquierdo"])

    preorden(raiz["derecho"])




def inorden(raiz):

    if raiz is None:

        return


    inorden(raiz["izquierdo"])

    print(raiz["codigo"])

    inorden(raiz["derecho"])




def postorden(raiz):

    if raiz is None:

        return


    postorden(raiz["izquierdo"])

    postorden(raiz["derecho"])

    print(raiz["codigo"])




def crear_arbol_desde_lista(codigos_misiones):

    raiz = None


    for codigo in codigos_misiones:

        raiz = insertar(
            raiz,
            codigo
        )


    return raiz




def actualizar_arbol_misiones():

    codigos_misiones = []

    for m in cola_misiones:

        codigos_misiones.append(
            m["codigo"]
        )


    return crear_arbol_desde_lista(
        codigos_misiones
    )



raiz_misiones = None




# BUSQUEDA LINEAL Y BINARIA


def buscar_dron_lineal(codigo_buscado):

    print(
        f"Buscando dron: {codigo_buscado}"
    )


    for i, dron in enumerate(drones_list):

        print(
            f"Comparando elemento {i+1}"
        )


        if dron["codigo"] == codigo_buscado:

            print("Encontrado")

            return dron



    print("No encontrado")

    return None




def buscar_mision_lineal(codigo_buscado):

    print(
        f"Buscando misión: {codigo_buscado}"
    )


    for i, mision in enumerate(cola_misiones):

        print(
            f"Comparando elemento {i+1}"
        )


        if mision["codigo"] == codigo_buscado:

            print("Encontrado")

            return mision



    print("No encontrado")

    return None




def ordenar_drones_por_codigo_insercion(drones):

    arreglo = []


    for d in drones:

        arreglo.append(d)



    n = len(arreglo)



    for i in range(1,n):

        clave = arreglo[i]

        j = i-1



        print(
            f"Insertando... Dron {clave['codigo']}"
        )


        while j >= 0 and arreglo[j]["codigo"] > clave["codigo"]:

            print(
                f"Moviendo... Dron {arreglo[j]['codigo']}"
            )


            arreglo[j+1] = arreglo[j]

            j -= 1



        arreglo[j+1] = clave



    return arreglo




def buscar_dron_binaria(codigo_buscado):

    if not drones_list:

        print("No hay drones registrados")

        return None



    drones_ordenados = ordenar_drones_por_codigo_insercion(
        drones_list
    )


    low = 0

    high = len(drones_ordenados)-1



    while low <= high:


        mid = (low+high)//2


        valor_medio = drones_ordenados[mid]["codigo"]



        print(f"low: {low}")

        print(f"high: {high}")

        print(f"mid: {mid}")

        print(
            f"valor medio: {valor_medio}"
        )



        if valor_medio == codigo_buscado:

            print("Encontrado")

            return drones_ordenados[mid]



        elif codigo_buscado < valor_medio:

            high = mid-1


        else:

            low = mid+1



    print("No encontrado")

    return None



# Grafo de zonas

def agregar_zona(zona):

    if zona not in grafo_zonas:

        grafo_zonas[zona] = []

        print(f"Zona agregada: {zona}")

    else:

        print(f"La zona {zona} ya existe.")


def agregar_ruta(zona1, zona2, distancia):

    if zona1 not in grafo_zonas:
        agregar_zona(zona1)

    if zona2 not in grafo_zonas:
        agregar_zona(zona2)

    grafo_zonas[zona1].append((zona2, distancia))
    grafo_zonas[zona2].append((zona1, distancia))

    print(f"Ruta agregada: {zona1} -- {distancia}km -- {zona2}")


def mostrar_grafo():

    print("\n===== GRAFO DE ZONAS =====")

    if len(grafo_zonas) == 0:
        print("El grafo esta vacio.")
        return

    for zona in grafo_zonas:

        conexiones = grafo_zonas[zona]

        texto_conexiones = ""

        for vecino, distancia in conexiones:
            texto_conexiones += f"{vecino} ({distancia}km)  "

        print(f"{zona} -> {texto_conexiones}")



# BFS Y Dijkstra


def bfs_existe_camino(inicio, destino):

    print(f"\n--- BFS: {inicio} -> {destino} ---")

    if inicio not in grafo_zonas or destino not in grafo_zonas:
        print("Una de las zonas no existe en el grafo.")
        return False, []

    visitados = []
    cola = [inicio]
    padres = {inicio: None}

    while len(cola) > 0:

        actual = cola.pop(0)

        print(f"Visitando: {actual}")

        if actual == destino:

            camino = []
            nodo = destino

            while nodo is not None:
                camino.append(nodo)
                nodo = padres[nodo]

            camino_ordenado = []
            for i in range(len(camino) - 1, -1, -1):
                camino_ordenado.append(camino[i])

            print("Camino encontrado:", camino_ordenado)

            return True, camino_ordenado

        if actual not in visitados:

            visitados.append(actual)

            print(f"Cola actual: {cola}")
            print(f"Nodos visitados: {visitados}")

            for vecino, distancia in grafo_zonas[actual]:

                if vecino not in visitados and vecino not in cola:

                    cola.append(vecino)
                    padres[vecino] = actual

    print("No existe camino entre las zonas.")

    return False, []

# Dijkstra

def dijkstra(inicio, destino):

    print(f"\n--- DIJKSTRA: {inicio} -> {destino} ---")

    if inicio not in grafo_zonas or destino not in grafo_zonas:
        print("Una de las zonas no existe en el grafo.")
        return None, None

    distancias = {}
    anteriores = {}
    visitados = []

    for zona in grafo_zonas:
        distancias[zona] = float("inf")
        anteriores[zona] = None

    distancias[inicio] = 0

    while len(visitados) < len(grafo_zonas):

        nodo_actual = None
        menor_distancia = float("inf")

        for zona in grafo_zonas:

            if zona not in visitados and distancias[zona] < menor_distancia:

                menor_distancia = distancias[zona]
                nodo_actual = zona

        if nodo_actual is None:
            break

        visitados.append(nodo_actual)

        print(f"\nNodo actual: {nodo_actual}")
        print(f"Distancias: {distancias}")

        for vecino, peso in grafo_zonas[nodo_actual]:

            nueva_distancia = distancias[nodo_actual] + peso

            if nueva_distancia < distancias[vecino]:

                distancias[vecino] = nueva_distancia
                anteriores[vecino] = nodo_actual

                print(f"  Ruta parcial: {nodo_actual} -> {vecino} = {nueva_distancia}km")

    ruta = []
    nodo = destino

    while nodo is not None:
        ruta.append(nodo)
        nodo = anteriores[nodo]

    ruta_final = []
    for i in range(len(ruta) - 1, -1, -1):
        ruta_final.append(ruta[i])

    print(f"\nRuta final: {' -> '.join(ruta_final)}")
    print(f"Distancia total: {distancias[destino]}km")

    return ruta_final, distancias[destino]


def mostrar_menu():

    print("\n===== MENÚ DE FUNCIONES =====")

    print("1. Registrar dron")
    print("2. Agregar misión a la cola")
    print("3. Atender misión de la cola")
    print("4. Mostrar siguiente misión")
    print("5. Buscar dron disponible")
    print("6. Ordenar drones por batería")
    print("7. Ordenar misiones por prioridad (Burbuja)")
    print("8. Mostrar recorrido Preorden")
    print("9. Mostrar recorrido Inorden")
    print("10. Mostrar recorrido Postorden")
    print("11. Buscar misión en el árbol")
    print("12. Búsqueda lineal de dron")
    print("13. Búsqueda lineal de misión")
    print("14. Búsqueda binaria de dron")
    print("15. Agregar zona")
    print("16. Agregar ruta entre zonas")
    print("17. Mostrar grafo")
    print("18. Verificar camino")
    print("19. Calcular ruta minima ")
    print("20. Simulacion completa de rescate")
    print("21. Salir")


def ejecutar_menu():

    global raiz_misiones

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            codigo = input("Código del dron: ")
            modelo = input("Modelo: ")
            velocidad = float(input("Velocidad: "))
            capacidad = int(input("Capacidad: "))
            bateria = float(input("Batería: "))

            registrar_dron(codigo, modelo, velocidad, capacidad, bateria)

            print("Dron registrado.")

        elif opcion == "2":

            codigo = input("Código de la misión: ")
            zona = input("Zona: ")
            tipo = input("Tipo de emergencia: ")
            prioridad = int(input("Prioridad (1 Alta, 2 Media, 3 Baja): "))
            personas = int(input("Personas afectadas: "))
            distancia = float(input("Distancia km: "))

            agregar_mision_a_cola(codigo, zona, tipo, prioridad, personas, distancia)

            raiz_misiones = actualizar_arbol_misiones()

            print("Misión agregada.")

        elif opcion == "3":

            atender_mision_de_cola()
            raiz_misiones = actualizar_arbol_misiones()

        elif opcion == "4":

            mostrar_siguiente_mision()

        elif opcion == "5":

            buscar_dron_disponible()

        elif opcion == "6":

            lista = ordenar_drones_por_bateria_insercion()

            print("Drones ordenados por batería:")

            for d in lista:
                print(d["codigo"], "-", d["bateria"], "%")

        elif opcion == "7":

            misiones = burbuja_prioridad(cola_misiones)

            print("\nMisiones ordenadas por prioridad:")

            for m in misiones:
                print(m["codigo"], "- Prioridad:", m["prioridad"])

        elif opcion == "8":

            print("Recorrido Preorden:")
            preorden(raiz_misiones)

        elif opcion == "9":

            print("Recorrido Inorden:")
            inorden(raiz_misiones)

        elif opcion == "10":

            print("Recorrido Postorden:")
            postorden(raiz_misiones)

        elif opcion == "11":

            codigo = input("Ingrese código de misión: ")
            buscar(raiz_misiones, codigo)

        elif opcion == "12":

            codigo = input("Ingrese código del dron: ")
            buscar_dron_lineal(codigo)

        elif opcion == "13":

            codigo = input("Ingrese código de misión: ")
            buscar_mision_lineal(codigo)

        elif opcion == "14":

            codigo = input("Ingrese código del dron: ")
            buscar_dron_binaria(codigo)

        elif opcion == "15":

            zona = input("Nombre de la zona: ")
            agregar_zona(zona)

        elif opcion == "16":

            zona1 = input("Zona 1: ")
            zona2 = input("Zona 2: ")
            distancia = float(input("Distancia (km): "))
            agregar_ruta(zona1, zona2, distancia)

        elif opcion == "17":

            mostrar_grafo()

        elif opcion == "18":

            inicio = input("Zona de inicio: ")
            destino = input("Zona destino: ")
            bfs_existe_camino(inicio, destino)

        elif opcion == "19":

            inicio = input("Zona de inicio: ")
            destino = input("Zona destino: ")
            dijkstra(inicio, destino)

        elif opcion == "20":

            zona_destino = input("Zona afectada: ")

            existe, camino = bfs_existe_camino("Base", zona_destino)

            if existe:

                dron = buscar_dron_disponible()
                ruta, distancia_total = dijkstra("Base", zona_destino)

                nombre_dron = dron["codigo"] if dron else "---"

                print(f"\nDron {nombre_dron} enviado por: {' -> '.join(ruta)}")
                print(f"Distancia total: {distancia_total} km")

            else:

                print("No hay ruta disponible hacia esa zona.")

        elif opcion == "21":

            print("Saliendo del menú...")
            break

        else:

            print("Opción inválida.")


ejecutar_menu()