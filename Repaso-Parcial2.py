

#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#INVENTARIO DE PRODUCTOS    
#CREAR UN PROGRAMA QUE PERMITA GESTIONAR UN INVENTARIOS DE PRODUCTOS. 
# CADA PRODUCTO TIENE NOMBRE, CANTIDAD, PRECIO 

#Funcionalidades: 
"""
- Agregar un nuevo producto al inventario.
- Actualizar la cantidad de un producto existente.
- Mostrar todos los productos con su cantidad y precio.
- Calcular el valor total del inventario."""

productos={"tomates":[7,5000],"papitas":[10,3500]}
print(productos)

def agregarProduc():
    print("Ingrese nombre del producto:")
    pro=input()
    print("Ingrese cantidad del producto:")
    cant=int(input())
    print("Ingrese precio del producto:")
    price=int(input())
    productos[pro]=[cant,price] #agrega el item con clave "pro": elementos de precio y cantidad con el "=[cant,price]"
    print(productos)

def actualizarProExis():

    print("A que producto le desea actualizar la cantidad en inventario?")
    produc=input()
    inven=productos.get(produc, "El producto no existe") #se busca si la variable produc corresponde a alguna clave guardada en el diccionario si es asi nos muestra sus valores, sino se muestra el valor por defecto de "El producto no existe"
    print(inven)

    newInven=int(input(f"Ingrese la nueva cantidad del producto {produc}: "))
    productos[produc][0]=newInven #para editar solo un valor de la lista del diccionario, damos el valor de su ubicacion, para que solo se edite ese dato 
    print(productos)

def mostrarProductos():
    print("\n")
    for k,v in productos.items(): # el metodo me retorna la dupla, la cual asigno a esas dos variables k y v
        print(f"El producto '{k}' con una cantidad en stock de '{v[0]}' y un precio unitaro de '{v[1]}'") 
        #aqui recorremos la dupla clave valor, como valor es una lista y queremos mostrar sus elementos en momentos diferentes 
        #usamos la ubicacion en la lista de ese elemento, con el v[posicion de la lista]

def valorInventario():
    preciounita=0
    total=0
    for v in productos.values(): #el metodo retorna solo los valores del diccionario y se van recorriendo con la variable v
        precio=v[1] #como los valores son una lista, solo queremos el valor de los precios, son la segunda posicion de la lista, lo asignamos a una variable mas
        preciounita=preciounita+precio
        cant=v[0] #como los valores son una lista, solo queremos el valor de cantidad, es la primera posicion de la lista, lo asignamos a una variable mas
        total=precio*cant+total
    print(f"El valor total de los productos unitarios es: {preciounita}$")
    print(f"El valor total de los productos es: {total}$")
    
while True: #menu tradicional
    print("\n--------------- Gestion de productos ----------------\n")
    print("Stock actual: ")
    print(productos)
    print("\nQue desea realizar?\n")
    print("1. Agregar un nuevo producto al inventario.")
    print("2. Actualizar la cantidad de un producto existente.")
    print("3. Mostrar todos los productos con su cantidad y precio.")
    print("4. Calcular el valor total del inventario.")
    print("5. Salir\n")

    opcion=int(input("Su eleccion es: "))

    if(opcion==1):
        agregarProduc()
    elif(opcion==2):
        actualizarProExis()
    elif(opcion==3):
        mostrarProductos()
    elif(opcion==4):
        valorInventario()
    elif(opcion==5):
        print("Saliendo del programa...")
        break
    else:
        print("La opcion seleccionada no es valida\n vuelva a ingresar los datos. ")


#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
        
"""Matriz de puntuaciones 
Escribe un programa que maneje las puntuaciones de varios jugadores en diferentes 
rondas de un juego. Usa una matriz (lista de listas) donde cada fila representa a un 
jugador y cada columna una ronda.

Funcionalidades:
-Calcular el puntaje total de cada jugador.
-Determinar el jugador con el mayor puntaje total.
-Mostrar los puntajes ordenados por ronda."""

def calcular_puntajes_totales(matriz):
    # Calcula el puntaje total de cada jugador sumando los elementos de su fila
    return [sum(jugador) for jugador in matriz]

def jugador_con_mayor_puntaje(puntajes_totales):
    # Encuentra el puntaje máximo de la lista de puntajes totales
    max_puntaje = max(puntajes_totales)
    # Retorna el índice del jugador con mayor puntaje y el puntaje máximo
    return puntajes_totales.index(max_puntaje), max_puntaje

def puntajes_ordenados_por_ronda(matriz):
    # Transpone la matriz para acceder a los puntajes por ronda y los ordena
    return [sorted(ronda) for ronda in zip(*matriz)] #el zip(*matriz) lo que hace es convertir las filas en columnas, asi cada fila representa los puntajes de una ronda

def main():
    # Ejemplo de matriz de puntuaciones: 3 jugadores y 4 rondas
    matriz = [
        [10, 20, 30, 40],  # Puntuaciones del Jugador 1
        [15, 25, 35, 10],  # Puntuaciones del Jugador 2
        [5,  10, 15, 20]   # Puntuaciones del Jugador 3
    ]

    # Muestra la matriz inicial de puntuaciones
    print("Matriz de puntuaciones:")
    for fila in matriz:
        print(fila)

    # Calcular puntajes totales de todos los jugadores
    puntajes_totales = calcular_puntajes_totales(matriz)
    print("\nPuntaje total de cada jugador:", puntajes_totales)

    # Determinar el jugador con el mayor puntaje total
    jugador_max, max_puntaje = jugador_con_mayor_puntaje(puntajes_totales)
    print(f"\nEl jugador con mayor puntaje total es el Jugador {jugador_max + 1} con {max_puntaje} puntos.")

    # Mostrar los puntajes ordenados por cada ronda
    puntajes_por_ronda = puntajes_ordenados_por_ronda(matriz)
    print("\nPuntajes ordenados por ronda:")
    for i, ronda in enumerate(puntajes_por_ronda): #enumerate retorna el indice y el valor del elemento actual "ronda"
        print(f"Ronda {i + 1}: {ronda}")


main()


#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]


"""Estadísticas de un grupo de personas (Listas y tuplas)
Escribe un programa que almacene los datos de varias personas 
en una lista de tuplas. Cada tupla debe contener: nombre, edad y ciudad.

Funcionalidades:
Mostrar las personas mayores de una edad específica.
Buscar personas por su ciudad.
Calcular la edad promedio del grupo.

"""
# Lista inicial de personas (tuplas con nombre, edad y ciudad)
personas = [
    ("Juan", 25, "Bogotá"),
    ("Ana", 30, "Medellín"),
    ("Luis", 22, "Cali"),
    ("Sofía", 35, "Bogotá")
]

def mostrar_mayores_edad():
    edad_minima = int(input("Ingrese la edad mínima: "))
    print(f"Personas mayores de {edad_minima} años:")
    for nombre, edad, ciudad in personas:  # Iteramos por cada tupla de la lista
        if edad > edad_minima:  # Verificamos si la edad supera la mínima
            print(f"- {nombre}, {edad} años, vive en {ciudad}")


def buscar_por_ciudad():
    ciudad_buscada = input("Ingrese la ciudad que desea buscar: ").capitalize() #.capitalice convierte la primera letyra en mayuscula y las demas en minusculas dentro de una cadena 
    print(f"Personas que viven en {ciudad_buscada}:")
    encontrados = False
    for nombre, edad, ciudad in personas:  # Recorremos cada persona
        if (ciudad == ciudad_buscada):  # Si la ciudad coincide
            print(f"- {nombre}, {edad} años")
            encontrados = True
    if not encontrados:
        print("No se encontraron personas en esa ciudad.")

def calcular_promedio_edad():
    total_edades = sum(edad for _, edad, _ in personas)  # Sumamos todas las edades, los _ representan los demas datos de la tupla que no interesan
    promedio = total_edades / len(personas)  # Dividimos por el número de personas, el len es usado para conocer la cantidad de personas dentro de la tupla
    print(f"La edad promedio del grupo es: {promedio:.2f} años.") #promedio: .2f  muestra el valor con dos decimas 

# Menú principal para interactuar con el usuario
while True:
    print("\n--- Estadísticas del grupo de personas ---")
    print("1. Mostrar personas mayores de una edad específica")
    print("2. Buscar personas por su ciudad")
    print("3. Calcular la edad promedio del grupo")
    print("4. Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            mostrar_mayores_edad()
        elif opcion == 2:
            buscar_por_ciudad()
        elif opcion == 3:
            calcular_promedio_edad()
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    except ValueError:
        print("Debe ingresar un número válido.")



#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]


"""Administración de una lista de tareas (Listas y tuplas)
Crea un programa que permita administrar una lista de tareas. 
Cada tarea debe tener un nombre, fecha de vencimiento y estado (pendiente o completada).

Funcionalidades:
Agregar una nueva tarea.
Marcar una tarea como completada.
Mostrar todas las tareas pendientes.
Mostrar las tareas ordenadas por fecha."""

# Lista inicial para almacenar las tareas
# Cada tarea se representa como una tupla: (nombre, fecha, estado)
tareas = [
    ("Estudiar matemáticas", "2025-02-10", "pendiente"),
    ("Comprar alimentos", "2025-02-09", "completada")
]

# Función para agregar una nueva tarea
def agregar_tarea():
    print("Ingrese el nombre de la nueva tarea:")
    nombre = input()
    print("Ingrese la fecha de vencimiento (YYYY-MM-DD):")
    fecha = input()
    estado = "pendiente"  # Las nuevas tareas siempre inician como pendientes
    tareas.append((nombre, fecha, estado))
    print(f"Tarea '{nombre}' agregada exitosamente.")

# Función para marcar una tarea como completada
def marcar_completada():
    print("Ingrese el nombre de la tarea que desea marcar como completada:")
    nombre = input()
    for i, tarea in enumerate(tareas): #enumerate nos da el indice y el contenido de cada tarea 
        if tarea[0].lower() == nombre.lower():
            tareas[i] = (tarea[0], tarea[1], "completada") #se actualiza la tupla en posicion i
            print(f"Tarea '{nombre}' marcada como completada.")
            return
    print("Tarea no encontrada.")

# Función para mostrar todas las tareas pendientes
def mostrar_pendientes():
    print("\nTareas pendientes:")
    for tarea in tareas:
        if tarea[2] == "pendiente": #si el indice 2 que corresponde al tercer elemento de la tupla (pendiente o completado) es igual a "pendiente " se ejecuta el condicional
            print(f"- {tarea[0]} (Vence el {tarea[1]})")

# Función para mostrar las tareas ordenadas por fecha
def mostrar_ordenadas_por_fecha():
    print("\nTareas ordenadas por fecha de vencimiento:")
    tareas_ordenadas = sorted(tareas, key=lambda x: x[1]) #el key=lambda x:x[1] significa que el ordenamiento se hace respecto al indice 1 de cada tupla, que corresponde al tiempo de vencimiento 
    for tarea in tareas_ordenadas:
        print(f"- {tarea[0]} (Vence el {tarea[1]} - Estado: {tarea[2]})")

# Menú principal
while True:
    print("\n----- Gestión de Lista de Tareas -----")
    print("1. Agregar una nueva tarea")
    print("2. Marcar una tarea como completada")
    print("3. Mostrar todas las tareas pendientes")
    print("4. Mostrar las tareas ordenadas por fecha")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        marcar_completada()
    elif opcion == "3":
        mostrar_pendientes()
    elif opcion == "4":
        mostrar_ordenadas_por_fecha()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")








