import pygame
import sys
import random

pygame.init()

ancho=800
alto=600
azul=(0,0,150)
gris=(100,100,100)
rojo=(200,0,0)
blanco=(255,255,255)
negro=(0,0,0)
verde=(0,190,0)

COLOR_BARCO = (75, 75, 75)
COLOR_HUNDIDO = (200, 0, 0)
COLOR_AGUA = (0, 100, 200)

#Dimensiones 
#tablero
tam_tablero=7 #10x10
tam_celda=50 #Tamaño del cuadrado en pixeles
inicioX=(ancho-(tam_tablero*tam_celda))//2
inicioY=(alto-(tam_tablero*tam_celda))//2+40

#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

#---------------------------------Configuracion de la ventana -------------------------------------
ventana=pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Batalla Naval - UN") #Nombre de la ventana

#Fondos e imagenes-------------------------------------------------
fondo=pygame.image.load("Fondo 1 - 8 bits.jpg") #Ruta de acceso de la imagen
fondo2=pygame.image.load("Fondo 2 - 8 Bits.jpg")

icono=pygame.image.load("Icono.jpg")
pygame.display.set_icon(icono)

fondoTablero=pygame.image.load("Fondo Tablero.jpg") #fondo tablero

#Fuentes----------------------------------------------------------
pygame.font.init()
Fuente_titulo=pygame.font.Font(None,50) #crecion de la fuente del titulo - none fuente predeterminada- 50 tamaño
Fuente_opcion=pygame.font.Font(None,55)
Fuente_Principal=pygame.font.Font(None,65)
letras_Tablero=pygame.font.Font(None,40) #fuente letras encima del tablero


#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

#----------------------------------------------Pantalla Inicial-------------------------------------------

#funciones para dibujar el texto de la pantalla inicial y sus botones
def NombreTitulo(textoTitulo,Fuente_Principal,color,ventana,x,y):
    principalTitulo=Fuente_Principal.render(textoTitulo,True,color)
    ajuste=principalTitulo.get_rect(center=(x,y))
    ventana.blit(principalTitulo, ajuste)

def OpcionesMenu(textoOpcion,Fuente_opcion,color,colorRect,ventana,x,y,anchoo,altoo):
    botonRectangulo=pygame.Rect(x,y,anchoo,altoo)
    pygame.draw.rect(ventana,colorRect,botonRectangulo) #dibujo del rectangulo - surface es la superficie donde se realiza el dibujo
    opcion=Fuente_opcion.render(textoOpcion,True,color) #creacion del texto
    textoRectangulo=opcion.get_rect(center=botonRectangulo.center) #centrar el texto en el rectangulo
    ventana.blit(opcion, textoRectangulo)
    return botonRectangulo

#buble de la pantallla inicial
def MenuPrincipal():
    while True:
        #ventana.fill(negro) #limpia la pantalla al inicio de cada iteracion de los bubles, borra lo dibujado anteriormente
        ventana.blit(fondo,(0,0))
        NombreTitulo("BATALLA NAVAL - INTERACTIVO",Fuente_Principal,azul,ventana,ancho//2,alto//6)
        #Dibujar botones
        BotonJuego=OpcionesMenu("Jugar",Fuente_opcion,azul,blanco,ventana,ancho//2-120,alto//2-75,250,80)
        BotonSalir=OpcionesMenu("Salir",Fuente_opcion,verde,blanco,ventana,ancho//2-120,alto//2+50,250,80)
        #Eventos
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()
            if(event.type==pygame.MOUSEBUTTONDOWN): #detecta el click
                posMou=pygame.mouse.get_pos() #optener posicion mouse
                if(BotonJuego.collidepoint(posMou)):#hace click en "jugar"
                    return "jugar"
                if(BotonSalir.collidepoint(posMou)):
                    pygame.quit()
                    sys.exit()
        pygame.display.flip()

#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

#---------------------------INCORPORACION DE BARCOS-----------------------------------

# Agrega en las constantes
tamañoBarcos = [4, 3, 3, 2, 2]  # Un barco de 3, dos de 2 y dos de 1

def crear_tablero():
    return {
        'celdas': [[0 for _ in range(tam_tablero)] for _ in range(tam_tablero)],
        'barcos': [],
        'intentos': set()
    }

# Función para colocar barcos
def colocarBarcosJugador(ventana):
    tablero = crear_tablero()
    
    for tamaño in tamañoBarcos:
        colocado = False
        direccion = 'H'
        
        while not colocado:
            ventana.blit(fondo2, (0,0))
            Tablero()
            dibujarBarcos(tablero, ventana)
            mostrarInstrucciones(tamaño, direccion)
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        direccion = 'H'
                    elif event.key == pygame.K_v:
                        direccion = 'V'
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    celda = ClickTablero(pos)
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
                            colocado = True
                            
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    return tablero

def validarPosicion(tablero, fila, col, tamaño, direccion):
    try:
        if direccion == 'H':
            # Verificar si cabe horizontalmente
            if col + tamaño > tam_tablero:
                return False
            # Verificar colisión con otros barcos
            return all(tablero[fila][col + i] == 0 for i in range(tamaño))
        else:
            # Verificar si cabe verticalmente
            if fila + tamaño > tam_tablero:
                return False
            # Verificar colisión con otros barcos
            return all(tablero[fila + i][col] == 0 for i in range(tamaño))
    except IndexError:
        return False

def colocarBarco(tablero, fila, col, tamaño, direccion):
    for i in range(tamaño):
        if direccion == 'H':
            tablero[fila][col + i] = 1
        else:
            tablero[fila + i][col] = 1

def dibujarBarcos(tablero, ventana):
    for fila in range(tam_tablero):
        for col in range(tam_tablero):
            if tablero[fila][col] == 1:
                x = inicioX + col * tam_celda
                y = inicioY + fila * tam_celda
                pygame.draw.rect(ventana, (75,75,75), (x+1, y+1, tam_celda-2, tam_celda-2))

def mostrarInstrucciones(tamaño, direccion):
    fuente = pygame.font.Font(None, 30)
    texto = fuente.render(f"Colocando barco de {tamaño} cuadros. Dirección: {direccion} (H/V)", True, negro)
    ventana.blit(texto, (50, 50))
    texto2 = fuente.render("Haz clic en la posición inicial", True, negro)
    ventana.blit(texto2, (50, 80))

#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

def manejar_disparo(tablero, fila, col):
    if (fila, col) in tablero['intentos']:
        return None  # Ya se disparó aquí
    
    tablero['intentos'].add((fila, col))
    
    if tablero['celdas'][fila][col] == 1:
        # Verificar si el barco está hundido
        for barco in tablero['barcos']:
            if (fila, col) in barco['posiciones']:
                barco['impactos'] += 1
                if barco['impactos'] == barco['tamaño']:
                    barco['hundido'] = True
                    return 'hundido'
                return 'impacto'
    return 'agua'


def dibujarBarcos(tablero, ventana):
    for fila in range(tam_tablero):
        for col in range(tam_tablero):
            x = inicioX + col * tam_celda
            y = inicioY + fila * tam_celda
            
            if tablero['celdas'][fila][col] == 1:
                # Dibujar barco (solo en tu propio tablero)
                pygame.draw.rect(ventana, COLOR_BARCO, (x+1, y+1, tam_celda-2, tam_celda-2))
            
            # Dibujar disparos
            if (fila, col) in tablero['intentos']:
                if tablero['celdas'][fila][col] == 1:
                    color = COLOR_HUNDIDO if any(barco['hundido'] for barco in tablero['barcos'] if (fila,col) in barco['posiciones']) else rojo
                else:
                    color = COLOR_AGUA
                pygame.draw.circle(ventana, color, (x + tam_celda//2, y + tam_celda//2), tam_celda//4)


#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]




#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

#---------------------------TABLERO-----------------------------------
#dibujar el tablero

fondoTablero=pygame.transform.scale(fondoTablero,(tam_tablero*tam_celda,tam_tablero*tam_celda))

def Tablero():
    ventana.blit(fondoTablero,(inicioX,inicioY)) # se coloca la imagen en la coordenada iniciox inicioy
    
    for fila in range(tam_tablero): #dibuja la lineas del tablero
        for columna in range(tam_tablero):
            x=inicioX+columna*tam_celda
            y=inicioY+fila*tam_celda
            pygame.draw.rect(ventana,negro,(x,y,tam_celda,tam_celda),1) #el 1 representa el valor de la linea divisoria del tablero

    letras="ABCDEFG" #PRIMERAS 10 LETRAS DE ABECEDARIO
    for columna in range(tam_tablero):
        x=inicioX+columna*tam_celda+tam_celda//2
        y=inicioY-30

        #agregar el texto
        letraEn=letras_Tablero.render(letras[columna],True,negro)
        ventana.blit(letraEn,(x-letraEn.get_width()//2,y))

    numero="1234567" #PRIMEROS 10 numeros
    for fila in range(tam_tablero):
        x=inicioX-30
        y=inicioY+fila*tam_celda+tam_celda//2

        #agregar el texto
        numeroEn=letras_Tablero.render(str(fila+1),True,negro)
        ventana.blit(numeroEn,(x,y-numeroEn.get_height()//2))
    
    """AgregarBarcos(ventana)"""


#detectar clicks del tablero
def ClickTablero(posicionT):
    xMouse, yMuose=posicionT
    for fila in range(tam_tablero):
        for columna in range(tam_tablero):
            x=inicioX+columna*tam_celda
            y=inicioY+fila*tam_celda
            ta=pygame.Rect(x,y,tam_celda,tam_celda)
            if(ta.collidepoint(xMouse,yMuose)):
                return fila, columna #retorna el valor de la fila y columna donde se hizo el click

#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

#----------------------------------------JUEGO BUCLE-------------------------------------
def JuegoLoop():

    tableroJugador=colocarBarcosJugador(ventana)
   
    titulo=Fuente_titulo.render("Batalla Naval",True, azul) #renderiza el texto con suavizado
    run=True
    while run:
        #ventana.fill(negro) #limpia la pantalla al inicio de cada iteracion de los bubles, borra lo dibujado anteriormente
        ventana.blit(fondo2,(0,0))
        Tablero() #Dibuja el tablero

        #Eventos-------------------------------------------------------------------------

        for evento in pygame.event.get(): #el pygame.event.get(), genera una lista de los eventos que ocurran dentro de la ventana 
            if(evento.type==pygame.QUIT): #si se cierra la ventana el progrmama lo interpreta cerrando el ciclo while
                run=False
            if(evento.type==pygame.MOUSEBUTTONDOWN): #evento del click
                click=ClickTablero(evento.pos) #Posicion del evento
                if(click):
                    fila,columna=click
                    print("Click en la celda: ",fila,columna)


        #Desarrollo juego-------------------------------------------------------------

        #titulo 
        ventana.blit(titulo,(ancho//2 - titulo.get_width()//2,20)) #(texto,(Coordenada x,y))
        pygame.draw.line(ventana,gris,(30,80),(ancho-30,80),2) #(30 valor de ancho, 80 alto), el 2 es el grosor

        dibujarBarcos(tableroJugador,ventana)

        #dibujar rectangulo

        """fuente=pygame.font.Font(None,33)
        texto=fuente.render(mensaje, True, blanco)
        ventana.blit(texto,(50,50))"""


        pygame.display.flip() #refresca la pantalla
    pygame.quit()#Salir del juego 
    sys.exit()#Salir del juego 

#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

#-----------------------------------------------------------------EJECUCION PRINCIPAL-------------------------
while True:
    modo=MenuPrincipal()
    if(modo=="jugar"):
        JuegoLoop()



