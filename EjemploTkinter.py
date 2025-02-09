import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
def ventana_principal():
    # Crear la instancia de la ventana principal
    ventana = tk.Tk()
    
    # Configuración básica de la ventana
    ventana.title("Ventana Básica con Tkinter")  # Título de la ventana
    ventana.geometry("400x400")  # Tamaño inicial de la ventana (ancho x alto)
    ventana.resizable(True, True)  # Permitir redimensionar la ventana
    ventana.config(bg="lightblue")  # Cambiar el color de fondo

    # Etiqueta (Label): para mostrar texto
    etiqueta = tk.Label(ventana, text="Bienvenido a Tkinter!", font=("Arial", 16), bg="lightblue")
    etiqueta.pack(pady=10)  # Empaquetar con margen vertical

    # Entrada de texto (Entry): para que el usuario ingrese datos
    entrada_texto = tk.Entry(ventana, font=("Arial", 14), width=25)
    entrada_texto.pack(pady=10)

    # Botón (Button): realiza una acción al ser presionado
    def mostrar_mensaje():
        texto = entrada_texto.get()  # Obtener el texto ingresado en la entrada
        if texto.strip():  # Verificar que no esté vacío
            messagebox.showinfo("Mensaje", f"Hola, {texto}!")
        else:
            messagebox.showerror("Error", "Por favor, escribe algo.")

    boton = tk.Button(ventana, text="Mostrar mensaje", font=("Arial", 14), command=mostrar_mensaje)
    boton.pack(pady=10)

    # Cuadro de selección (Checkbutton): para activar o desactivar opciones
    opcion_var = tk.BooleanVar()  # Variable booleana para almacenar el estado
    check_opcion = tk.Checkbutton(ventana, text="Acepto los términos", variable=opcion_var, bg="lightblue")
    check_opcion.pack(pady=10)

    # Lista desplegable (OptionMenu): para elegir una opción de una lista
    opciones = ["Opción 1", "Opción 2", "Opción 3"]  # Lista de opciones
    opcion_seleccionada = tk.StringVar(value=opciones[0])  # Variable para almacenar la selección
    lista_desplegable = tk.OptionMenu(ventana, opcion_seleccionada, *opciones)
    lista_desplegable.config(font=("Arial", 12))  # Configurar el estilo
    lista_desplegable.pack(pady=10)

    # Botón para mostrar la opción seleccionada
    def mostrar_opcion():
        messagebox.showinfo("Opción seleccionada", f"Elegiste: {opcion_seleccionada.get()}")

    boton_opcion = tk.Button(ventana, text="Mostrar opción", font=("Arial", 14), command=mostrar_opcion)
    boton_opcion.pack(pady=10)

    # Botón para salir de la aplicación
    def salir():
        ventana.destroy()

    boton_salir = tk.Button(ventana, text="Salir", font=("Arial", 14), bg="red", fg="white", command=salir)
    boton_salir.pack(pady=10)

    # Iniciar el bucle principal de la ventana
    ventana.mainloop()

# Llamar a la función para iniciar la ventana
ventana_principal()
