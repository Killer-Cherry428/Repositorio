#suma de dos matrices de tamaño n, ammbas deben poseer el mismo tamaño para poder realizar efectiva la suma

def sumar_matrices(matriz1, matriz2):
    # Verificar que las matrices tengan las mismas dimensiones
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]): #len(matriz) revisa filas , len(matriz[0]) revisa columnas
        raise ValueError("Las matrices deben tener las mismas dimensiones")

    # Crear una matriz resultante con las mismas dimensiones
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = [[0 for _ in range(columnas)] for _ in range(filas)] #se crea la matriz resultado, inicialmente es una matriz llena de 0

    # Sumar las matrices
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]

    return resultado

# Ejemplo de uso
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Sumar las matrices
resultado = sumar_matrices(matriz1, matriz2)

# Mostrar el resultado
print("Matriz 1:")
for fila in matriz1:
    print(fila)

print("\nMatriz 2:")
for fila in matriz2:
    print(fila)

print("\nResultado de la suma:")
for fila in resultado:
    print(fila)
