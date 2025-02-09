import tkinter as tk
from tkinter import messagebox

# Diccionario para almacenar los productos
productos = {"tomates": [7, 5000], "papitas": [10, 3500]}

# Función para agregar un nuevo producto
def agregar_producto():
    nombre = entry_nombre.get()
    cantidad = entry_cantidad.get()
    precio = entry_precio.get()

    if nombre and cantidad and precio:
        try:
            cantidad = int(cantidad)
            precio = int(precio)
            productos[nombre] = [cantidad, precio]
            messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado correctamente.")
            entry_nombre.delete(0, tk.END)
            entry_cantidad.delete(0, tk.END)
            entry_precio.delete(0, tk.END)
            actualizar_lista()
        except ValueError:
            messagebox.showerror("Error", "La cantidad y el precio deben ser números enteros.")
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")

# Función para actualizar la cantidad de un producto existente
def actualizar_cantidad():
    nombre = entry_actualizar_nombre.get()
    nueva_cantidad = entry_actualizar_cantidad.get()

    if nombre and nueva_cantidad:
        if nombre in productos:
            try:
                nueva_cantidad = int(nueva_cantidad)
                productos[nombre][0] = nueva_cantidad
                messagebox.showinfo("Éxito", f"Cantidad de '{nombre}' actualizada correctamente.")
                entry_actualizar_nombre.delete(0, tk.END)
                entry_actualizar_cantidad.delete(0, tk.END)
                actualizar_lista()
            except ValueError:
                messagebox.showerror("Error", "La cantidad debe ser un número entero.")
        else:
            messagebox.showerror("Error", f"El producto '{nombre}' no existe en el inventario.")
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")

# Función para mostrar todos los productos
def mostrar_productos():
    lista_productos.delete(0, tk.END)
    for producto, datos in productos.items():
        lista_productos.insert(tk.END, f"{producto}: Cantidad = {datos[0]}, Precio = {datos[1]}$")

# Función para calcular el valor total del inventario
def calcular_valor_total():
    total = 0
    for datos in productos.values():
        total += datos[0] * datos[1]
    messagebox.showinfo("Valor Total", f"El valor total del inventario es: {total}$")

# Función para actualizar la lista de productos en la interfaz
def actualizar_lista():
    mostrar_productos()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Inventario")
ventana.geometry("500x400")

# Crear y colocar los widgets en la ventana

# Sección para agregar un nuevo producto
frame_agregar = tk.LabelFrame(ventana, text="Agregar Producto", padx=10, pady=10)
frame_agregar.pack(fill="x", padx=10, pady=5)

tk.Label(frame_agregar, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(frame_agregar)
entry_nombre.grid(row=0, column=1)

tk.Label(frame_agregar, text="Cantidad:").grid(row=1, column=0)
entry_cantidad = tk.Entry(frame_agregar)
entry_cantidad.grid(row=1, column=1)

tk.Label(frame_agregar, text="Precio:").grid(row=2, column=0)
entry_precio = tk.Entry(frame_agregar)
entry_precio.grid(row=2, column=1)

tk.Button(frame_agregar, text="Agregar", command=agregar_producto).grid(row=3, column=0, columnspan=2)

# Sección para actualizar la cantidad de un producto existente
frame_actualizar = tk.LabelFrame(ventana, text="Actualizar Cantidad", padx=10, pady=10)
frame_actualizar.pack(fill="x", padx=10, pady=5)

tk.Label(frame_actualizar, text="Nombre:").grid(row=0, column=0)
entry_actualizar_nombre = tk.Entry(frame_actualizar)
entry_actualizar_nombre.grid(row=0, column=1)

tk.Label(frame_actualizar, text="Nueva Cantidad:").grid(row=1, column=0)
entry_actualizar_cantidad = tk.Entry(frame_actualizar)
entry_actualizar_cantidad.grid(row=1, column=1)

tk.Button(frame_actualizar, text="Actualizar", command=actualizar_cantidad).grid(row=2, column=0, columnspan=2)

# Sección para mostrar todos los productos
frame_lista = tk.LabelFrame(ventana, text="Lista de Productos", padx=10, pady=10)
frame_lista.pack(fill="both", expand=True, padx=10, pady=5)

lista_productos = tk.Listbox(frame_lista)
lista_productos.pack(fill="both", expand=True)

# Botón para calcular el valor total del inventario
tk.Button(ventana, text="Calcular Valor Total", command=calcular_valor_total).pack(pady=10)

# Mostrar la lista de productos al iniciar
actualizar_lista()

# Iniciar el bucle principal de la ventana
ventana.mainloop()