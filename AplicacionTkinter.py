import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal para el inventario
class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Inventario")
        self.root.geometry("500x500")
        self.root.config(bg="lightblue")

        # Diccionario para gestionar productos
        self.productos = {"tomates": [7, 5000], "papitas": [10, 3500]}

        # Crear widgets principales
        self.crear_widgets()

    def crear_widgets(self):
        # Etiqueta de título
        tk.Label(self.root, text="Inventario de Productos", font=("Arial", 18), bg="lightblue").pack(pady=10)

        # Botones para funcionalidades
        tk.Button(self.root, text="Agregar Producto", font=("Arial", 14), command=self.agregar_producto).pack(pady=5)
        tk.Button(self.root, text="Actualizar Cantidad", font=("Arial", 14), command=self.actualizar_producto).pack(pady=5)
        tk.Button(self.root, text="Mostrar Productos", font=("Arial", 14), command=self.mostrar_productos).pack(pady=5)
        tk.Button(self.root, text="Calcular Valor Total", font=("Arial", 14), command=self.calcular_valor_total).pack(pady=5)
        tk.Button(self.root, text="Salir", font=("Arial", 14), bg="red", fg="white", command=self.root.quit).pack(pady=5)

    def agregar_producto(self):
        # Ventana emergente para agregar un producto
        def agregar():
            nombre = entrada_nombre.get()
            cantidad = entrada_cantidad.get()
            precio = entrada_precio.get()
            if nombre and cantidad.isdigit() and precio.isdigit():
                self.productos[nombre] = [int(cantidad), int(precio)]
                messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado correctamente!")
                ventana_agregar.destroy()
            else:
                messagebox.showerror("Error", "Datos inválidos, intente nuevamente.")

        ventana_agregar = tk.Toplevel(self.root)
        ventana_agregar.title("Agregar Producto")
        ventana_agregar.geometry("300x200")

        tk.Label(ventana_agregar, text="Nombre del Producto:").pack(pady=5)
        entrada_nombre = tk.Entry(ventana_agregar)
        entrada_nombre.pack(pady=5)

        tk.Label(ventana_agregar, text="Cantidad:").pack(pady=5)
        entrada_cantidad = tk.Entry(ventana_agregar)
        entrada_cantidad.pack(pady=5)

        tk.Label(ventana_agregar, text="Precio:").pack(pady=5)
        entrada_precio = tk.Entry(ventana_agregar)
        entrada_precio.pack(pady=5)

        tk.Button(ventana_agregar, text="Agregar", command=agregar).pack(pady=10)

    def actualizar_producto(self):
        # Ventana emergente para actualizar un producto existente
        def actualizar():
            nombre = entrada_nombre.get()
            nueva_cantidad = entrada_cantidad.get()
            if nombre in self.productos and nueva_cantidad.isdigit():
                self.productos[nombre][0] = int(nueva_cantidad)
                messagebox.showinfo("Éxito", f"Cantidad de '{nombre}' actualizada correctamente!")
                ventana_actualizar.destroy()
            else:
                messagebox.showerror("Error", "Producto no encontrado o cantidad inválida.")

        ventana_actualizar = tk.Toplevel(self.root)
        ventana_actualizar.title("Actualizar Producto")
        ventana_actualizar.geometry("300x150")

        tk.Label(ventana_actualizar, text="Nombre del Producto:").pack(pady=5)
        entrada_nombre = tk.Entry(ventana_actualizar)
        entrada_nombre.pack(pady=5)

        tk.Label(ventana_actualizar, text="Nueva Cantidad:").pack(pady=5)
        entrada_cantidad = tk.Entry(ventana_actualizar)
        entrada_cantidad.pack(pady=5)

        tk.Button(ventana_actualizar, text="Actualizar", command=actualizar).pack(pady=10)

    def mostrar_productos(self):
        # Ventana emergente para mostrar todos los productos
        ventana_mostrar = tk.Toplevel(self.root)
        ventana_mostrar.title("Productos en Inventario")
        ventana_mostrar.geometry("400x300")

        for nombre, datos in self.productos.items():
            cantidad, precio = datos
            tk.Label(ventana_mostrar, text=f"{nombre}: Cantidad: {cantidad}, Precio: {precio}").pack(pady=2)

    def calcular_valor_total(self):
        # Calcular el valor total del inventario
        total = sum(cantidad * precio for cantidad, precio in self.productos.values())
        messagebox.showinfo("Valor Total", f"El valor total del inventario es: ${total}")

# Inicializar la aplicación principal
if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()
