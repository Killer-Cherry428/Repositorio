import pygame, sys, random, time, re
import firebase_admin
from firebase_admin import credentials, db

# -------------------------- Firebase -----------------------------
# Inicializar Firebase con tu certificado y URL
cred = credentials.Certificate(r"C:\Users\User\Documents\Visual Studio Code - Programación\Python\Firebase\Firebase compartido - Batalla naval\bookstoreproject-8b4f0-firebase-adminsdk-2eymv-b7972991ba.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://bookstoreproject-8b4f0-default-rtdb.firebaseio.com/"
})
# Referencia a la sala de juego
sala_ref = db.reference("salas/partida1")

def guardar_datos_jugador(jugador, datos_personales, coordenadas_barcos):
    data = {
        "datos_personales": datos_personales,
        "barcos": coordenadas_barcos,
        "disparos": []
    }
    sala_ref.child(jugador).set(data)

def esperar_oponente():
    # Espera a que ambos jugadores se hayan registrado
    while True:
        sala = sala_ref.get()
        if sala and "jugador1" in sala and "jugador2" in sala:
            print("Ambos jugadores están listos.")
            break
        print("Esperando al otro jugador...")
        time.sleep(1)

def obtener_barcos_oponente(jugador_actual):
    oponente = "jugador2" if jugador_actual == "jugador1" else "jugador1"
    data = sala_ref.child(oponente).get()
    if data:
        return data.get("barcos", [])
    return []

def registrar_disparo(jugador, coordenada):
    disparos_ref = sala_ref.child(jugador).child("disparos")
    disparos_ref.push(coordenada)

def set_turno(turno):
    sala_ref.child("turno").set(turno)

def get_turno():
    return sala_ref.child("turno").get()

def switch_turn(jugador_actual):
    nuevo_turno = "jugador2" if jugador_actual == "jugador1" else "jugador1"
    set_turno(nuevo_turno)

# -------------------------- Registro de Usuario -----------------------------
def registrar_usuario_gui(jugador_num):
    datos = {"UserName": "", "Edad": "", "Correo": ""}
    campos = ["UserName", "Edad", "Correo"]
    campo_actual = 0
    texto_ingresado = ""
    activo = True
    mostrar_error = False
    error_msg = ""
    boton_confirmar = None

    while activo:
        ventana.blit(fondo2, (0, 0))
        
        # Título de registro
        NombreTitulo(f"Registro Jugador {jugador_num}", Fuente_Principal, azul, ventana, ancho//2, 100)

        # Dibujar cada campo de registro
        y = 200
        for i, campo in enumerate(campos):
            color = verde if i == campo_actual else gris
            # Si el campo está activo se muestra el texto que se está ingresando
            if i == campo_actual:
                contenido = texto_ingresado + "_"
            else:
                contenido = datos[campo]
            texto = Fuente_opcion.render(f"{campo}: {contenido}", True, color)
            ventana.blit(texto, (100, y + i * 60))

        # Dibujar botón de confirmación solo si todos los campos tienen datos
        if all(datos.values()):
            boton_confirmar = OpcionesMenu("Confirmar", Fuente_opcion, blanco, azul, ventana, ancho//2 - 100, 450, 200, 50)

        # Mostrar mensajes de error (si existen)
        if mostrar_error:
            error_texto = Fuente_opcion.render(error_msg, True, rojo)
            ventana.blit(error_texto, (100, 400))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Si es el campo de correo, validar el formato
                    if campo_actual == 2:
                        if not re.match(r"[^@]+@[^@]+\.[^@]+", texto_ingresado.strip()):
                            mostrar_error = True
                            error_msg = "Correo inválido!"
                            continue
                    # Guardar el texto ingresado en el campo actual
                    datos[campos[campo_actual]] = texto_ingresado.strip()
                    texto_ingresado = ""
                    mostrar_error = False
                    # Si no es el último campo, pasar al siguiente; de lo contrario, salir del ciclo
                    if campo_actual < len(campos) - 1:
                        campo_actual += 1
                    else:
                        activo = False
                        break

                elif event.key == pygame.K_BACKSPACE:
                    texto_ingresado = texto_ingresado[:-1]
                else:
                    texto_ingresado += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN and boton_confirmar is not None:
                pos = pygame.mouse.get_pos()
                if boton_confirmar.collidepoint(pos):
                    # Validación final: edad debe ser numérica y el correo debe tener formato correcto
                    if not datos["Edad"].isdigit():
                        mostrar_error = True
                        error_msg = "Edad debe ser numérica!"
                    elif not re.match(r"[^@]+@[^@]+\.[^@]+", datos["Correo"]):
                        mostrar_error = True
                        error_msg = "Correo inválido!"
                    else:
                        activo = False
                        break

    return f"jugador{jugador_num}", datos

# -------------------------- Configuración Pygame -----------------------------
pygame.init()

ancho = 800
alto = 600
azul = (0, 0, 150)
gris = (100, 100, 100)
rojo = (200, 0, 0)
blanco = (255, 255, 255)
negro = (0, 0, 0)
verde = (0, 190, 0)

COLOR_BARCO = (75, 75, 75)
COLOR_HUNDIDO = (200, 0, 0)
COLOR_AGUA = (0, 100, 200)

# Dimensiones del tablero
tam_tablero = 7
tam_celda = 40
inicioX = (ancho - (tam_tablero * tam_celda)) // 2
inicioY = (alto - (tam_tablero * tam_celda)) // 2 + 40

# Configurar la ventana
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Batalla Naval - UN")

# Cargar imágenes (asegúrate de tener estos archivos en la ruta correcta)
fondo = pygame.image.load("Fondo 1 - 8 bits.jpg")
fondo2 = pygame.image.load("Fondo 2 - 8 Bits.jpg")
icono = pygame.image.load("Icono.jpg")
pygame.display.set_icon(icono)
fondoTablero = pygame.image.load("Fondo Tablero.jpg")
fondoTablero = pygame.transform.scale(fondoTablero, (tam_tablero * tam_celda, tam_tablero * tam_celda))

# Fuentes
pygame.font.init()
Fuente_titulo = pygame.font.Font(None, 50)
Fuente_opcion = pygame.font.Font(None, 55)
Fuente_Principal = pygame.font.Font(None, 65)
letras_Tablero = pygame.font.Font(None, 40)

# -------------------------- Funciones de Menú e Interfaz -----------------------------
def NombreTitulo(textoTitulo, fuente, color, ventana, x, y):
    principalTitulo = fuente.render(textoTitulo, True, color)
    ajuste = principalTitulo.get_rect(center=(x, y))
    ventana.blit(principalTitulo, ajuste)

def OpcionesMenu(textoOpcion, fuente, color, colorRect, ventana, x, y, anchoo, altoo):
    botonRectangulo = pygame.Rect(x, y, anchoo, altoo)
    pygame.draw.rect(ventana, colorRect, botonRectangulo)
    opcion = fuente.render(textoOpcion, True, color)
    textoRectangulo = opcion.get_rect(center=botonRectangulo.center)
    ventana.blit(opcion, textoRectangulo)
    return botonRectangulo

def MenuPrincipal():
    while True:
        ventana.blit(fondo, (0, 0))
        NombreTitulo("BATALLA NAVAL - INTERACTIVO", Fuente_Principal, azul, ventana, ancho // 2, alto // 6)
        BotonJuego = OpcionesMenu("Jugar", Fuente_opcion, azul, blanco, ventana, ancho // 2 - 120, alto // 2 - 75, 250, 80)
        BotonSalir = OpcionesMenu("Salir", Fuente_opcion, verde, blanco, ventana, ancho // 2 - 120, alto // 2 + 50, 250, 80)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posMou = pygame.mouse.get_pos()
                if BotonJuego.collidepoint(posMou):
                    return "jugar"
                if BotonSalir.collidepoint(posMou):
                    pygame.quit()
                    sys.exit()
        pygame.display.flip()

# -------------------------- Funciones de Tablero y Barcos -----------------------------
tamañoBarcos = [4,3,3,2,2,1]

def crear_tablero():
    return {
        'celdas': [[0 for _ in range(tam_tablero)] for _ in range(tam_tablero)],
        'barcos': [],
        'intentos': set()
    }

def colocarBarcosJugador(ventana):
    tablero = crear_tablero()
    barcos_a_colocar = tamañoBarcos.copy()  # Copia la lista original
    
    while barcos_a_colocar:
        tamaño = barcos_a_colocar[0]
        colocado = False
        direccion = 'H'
        while not colocado:
            ventana.blit(fondo2, (0, 0))
            Tablero()  # Dibuja el fondo y la cuadrícula
            dibujarBarcosPropios(tablero, ventana)
            mostrarInstrucciones(tamaño, direccion, len(barcos_a_colocar))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        direccion = 'H'
                    elif event.key == pygame.K_v:
                        direccion = 'V'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    celda = ClickTablero(pos, inicioX, inicioY)
                    if celda:
                        fila, col = celda
                        if validarPosicion(tablero['celdas'], fila, col, tamaño, direccion):
                            barco = {
                                'posiciones': [],
                                'tamaño': tamaño,
                                'impactos': 0,
                                'hundido': False
                            }
                            for i in range(tamaño):
                                if direccion == 'H':
                                    tablero['celdas'][fila][col + i] = 1
                                    barco['posiciones'].append((fila, col + i))
                                else:
                                    tablero['celdas'][fila + i][col] = 1
                                    barco['posiciones'].append((fila + i, col))
                            tablero['barcos'].append(barco)
                            barcos_a_colocar.pop(0)  # Remover el barco colocado
                            colocado = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    return tablero

def validarPosicion(tablero, fila, col, tamaño, direccion):
    try:
        if direccion == 'H':
            if col + tamaño > tam_tablero:
                return False
            return all(tablero[fila][col + i] == 0 for i in range(tamaño))
        else:
            if fila + tamaño > tam_tablero:
                return False
            return all(tablero[fila + i][col] == 0 for i in range(tamaño))
    except IndexError:
        return False

def dibujarBarcosPropios(tablero, ventana):
    for fila in range(tam_tablero):
        for col in range(tam_tablero):
            x = inicioX + col * tam_celda
            y = inicioY + fila * tam_celda
            if tablero['celdas'][fila][col] == 1:
                pygame.draw.rect(ventana, COLOR_BARCO, (x+1, y+1, tam_celda-2, tam_celda-2))
            if (fila, col) in tablero['intentos']:
                if tablero['celdas'][fila][col] == 1:
                    color = COLOR_HUNDIDO if any(barco['hundido'] for barco in tablero['barcos'] if (fila, col) in barco['posiciones']) else rojo
                else:
                    color = COLOR_AGUA
                pygame.draw.circle(ventana, color, (x + tam_celda//2, y + tam_celda//2), tam_celda//4)

def mostrarInstrucciones(tamaño, direccion, barcos_restantes):
    fuente = pygame.font.Font(None, 30)
    textos = [
        f"Barcos restantes: {barcos_restantes}",
        f"Colocando barco de {tamaño} cuadros",
        f"Dirección: {direccion} (Presiona H/V para cambiar)",
        "Haz clic en la posición inicial"
    ]
    
    y = 50
    for texto in textos:
        render = fuente.render(texto, True, negro)
        ventana.blit(render, (50, y))
        y += 30

def Tablero():
    ventana.blit(fondoTablero, (inicioX, inicioY))
    for fila in range(tam_tablero):
        for columna in range(tam_tablero):
            x = inicioX + columna * tam_celda
            y = inicioY + fila * tam_celda
            pygame.draw.rect(ventana, negro, (x, y, tam_celda, tam_celda), 1)
    letras = "ABCDEFG"
    for columna in range(tam_tablero):
        x = inicioX + columna * tam_celda + tam_celda//2
        y = inicioY - 30
        letraEn = letras_Tablero.render(letras[columna], True, negro)
        ventana.blit(letraEn, (x - letraEn.get_width()//2, y))
    numero = "1234567"
    for fila in range(tam_tablero):
        x = inicioX - 30
        y = inicioY + fila * tam_celda + tam_celda//2
        numeroEn = letras_Tablero.render(str(fila+1), True, negro)
        ventana.blit(numeroEn, (x, y - numeroEn.get_height()//2))

def ClickTablero(posicionT, inicioX_tablero, inicioY_tablero):
    xMouse, yMouse = posicionT
    for fila in range(tam_tablero):
        for col in range(tam_tablero):
            x = inicioX_tablero + col * tam_celda
            y = inicioY_tablero + fila * tam_celda
            rect = pygame.Rect(x, y, tam_celda, tam_celda)
            if rect.collidepoint(xMouse, yMouse):
                return fila, col
    return None

def extraer_coordenadas_barcos(tablero):
    coords = []
    for barco in tablero['barcos']:
        coords.extend(barco['posiciones'])
    return coords

# -------------------------- Fase de Ataque -----------------------------
def JuegoAtaque(jugador_actual):
    clock = pygame.time.Clock()
    run = True
    mensaje = ""
    mensaje_tiempo = 0

    # Coordenadas para los dos tableros
    inicioX_defensa = 50
    inicioX_ataque = ancho//2 + 50
    inicioY_tableros = 150

    while run:
        ventana.blit(fondo2, (0, 0))
        turno_actual = get_turno()
        oponente = "jugador2" if jugador_actual == "jugador1" else "jugador1"
        
        # Obtener datos de Firebase
        disparos_jugador = sala_ref.child(jugador_actual).child("disparos").get() or []
        disparos_oponente = sala_ref.child(oponente).child("disparos").get() or []
        barcos_oponente = obtener_barcos_oponente(jugador_actual)
        mis_barcos = sala_ref.child(jugador_actual).child("barcos").get() or []

        # Dibujar título
        titulo = Fuente_titulo.render("Fase de Ataque", True, azul)
        ventana.blit(titulo, (ancho//2 - titulo.get_width()//2, 20))
        
        # Dibujar dos tableros
        dibujar_tablero_defensa(inicioX_defensa, inicioY_tableros, mis_barcos, disparos_oponente)
        dibujar_tablero_ataque(inicioX_ataque, inicioY_tableros, barcos_oponente, disparos_jugador)
        
        texto_defensa = Fuente_opcion.render("Tu Tablero", True, azul)
        ventana.blit(texto_defensa, (inicioX_defensa + 50, inicioY_tableros - 40))
    
        texto_ataque = Fuente_opcion.render("Tablero Enemigo", True, rojo)
        ventana.blit(texto_ataque, (inicioX_ataque + 30, inicioY_tableros - 40))

        # Mostrar mensajes
        if time.time() - mensaje_tiempo < 2:
            mensaje_texto = Fuente_opcion.render(mensaje, True, rojo)
            ventana.blit(mensaje_texto, (ancho//2 - mensaje_texto.get_width()//2, alto - 100))
        
        # Control de turnos
        if turno_actual == jugador_actual:
            texto_turno = Fuente_opcion.render("Tu turno", True, verde)
        else:
            texto_turno = Fuente_opcion.render("Turno del oponente", True, rojo)
        ventana.blit(texto_turno, (ancho//2 - texto_turno.get_width()//2, alto - 50))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and turno_actual == jugador_actual:
                pos = pygame.mouse.get_pos()
                celda = ClickTablero(pos, inicioX_ataque, inicioY_tableros)
                if celda:
                    fila, col = celda
                    # Verificar si ya se disparó aquí
                    if not any(d == [fila, col] for d in disparos_jugador):
                        resultado = "¡Impacto!" if [fila, col] in barcos_oponente else "Tiro fallido"
                        mensaje = resultado
                        mensaje_tiempo = time.time()
                        registrar_disparo(jugador_actual, [fila, col])
                        switch_turn(jugador_actual)
        
        clock.tick(30)
    pygame.quit()
    sys.exit()


# Funciones auxiliares para dibujar los tableros
def dibujar_tablero_defensa(x, y, barcos_propios, disparos_oponente):
    # Dibujar fondo del tablero
    ventana.blit(fondoTablero, (x, y)) 

    # Título del tablero
    texto_titulo = Fuente_opcion.render("Tus Barcos", True, azul)
    ventana.blit(texto_titulo, (x + (tam_tablero*tam_celda)//2 - texto_titulo.get_width()//2, y - 40))
    
    # Dibujar celdas y barcos
    for fila in range(tam_tablero):
        for col in range(tam_tablero):
            rect = pygame.Rect(x + col*tam_celda, y + fila*tam_celda, tam_celda, tam_celda)
            pygame.draw.rect(ventana, negro, rect, 1)
            
            # Mostrar TODOS los barcos propios
            if [fila, col] in barcos_propios:
                pygame.draw.rect(ventana, COLOR_BARCO, rect.inflate(-4, -4))
            
            # Mostrar impactos recibidos
            if any(d == [fila, col] for d in disparos_oponente):
                color = COLOR_HUNDIDO if [fila, col] in barcos_propios else COLOR_AGUA
                pygame.draw.circle(ventana, color, rect.center, 15)

def dibujar_tablero_ataque(x, y, barcos_oponente, disparos_jugador):
    # Dibujar fondo del tablero
    ventana.blit(fondoTablero, (x, y))    
    # Dibujar celdas y disparos
    for fila in range(tam_tablero):
        for col in range(tam_tablero):
            rect = pygame.Rect(x + col*tam_celda, y + fila*tam_celda, tam_celda, tam_celda)
            pygame.draw.rect(ventana, negro, rect, 1)
            
            # Mostrar disparos realizados
            if any(d == [fila, col] for d in disparos_jugador):
                color = rojo if [fila, col] in barcos_oponente else COLOR_AGUA
                pygame.draw.circle(ventana, color, rect.center, 15)

# -------------------------- Flujo Principal -----------------------------
def ejecicionPrincipal():
    # Menú principal con Pygame
    while True:
        modo = MenuPrincipal()
        if modo == "jugar":
            # Selección de jugador
            ventana.blit(fondo2, (0,0))
            NombreTitulo("Selecciona tu jugador", Fuente_Principal, azul, ventana, ancho//2, 100)
            boton_j1 = OpcionesMenu("Jugador 1", Fuente_opcion, blanco, azul, ventana, ancho//2 - 150, 250, 200, 50)
            boton_j2 = OpcionesMenu("Jugador 2", Fuente_opcion, blanco, azul, ventana, ancho//2 + 50, 250, 200, 50)
            pygame.display.flip()

            jugador_num = None
            while not jugador_num:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if boton_j1.collidepoint(pos):
                            jugador_num = 1
                        elif boton_j2.collidepoint(pos):
                            jugador_num = 2

            jugador_actual, datos_jugador = registrar_usuario_gui(jugador_num)
            
            # Resto del flujo del juego...
            tablero = colocarBarcosJugador(ventana)
            coordenadas_barcos = extraer_coordenadas_barcos(tablero)
            guardar_datos_jugador(jugador_actual, datos_jugador, coordenadas_barcos)
            esperar_oponente()
            
            if get_turno() is None:
                set_turno("jugador1" if jugador_num == 1 else "jugador2")
            
            JuegoAtaque(jugador_actual)

def mostrar_error(mensaje):
    ventana.blit(fondo2, (0,0))
    texto = Fuente_Principal.render(mensaje, True, rojo)
    ventana.blit(texto, (100, 300))
    pygame.display.flip()
    pygame.time.wait(3000)

ejecicionPrincipal()
