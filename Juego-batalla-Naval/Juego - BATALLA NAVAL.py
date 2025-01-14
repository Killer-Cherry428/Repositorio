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

#Dimensiones 
#tablero
tam_tablero=10 #10x10
tam_celda=40 #Tamaño del cuadrado en pixeles
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

"""def AgregarBarcos(ventana):
    barcos=[]

    #dimensiones de los barcos
    barcosDimensiones=[(5,1),(4,1),(3,1),(3,1),(2,1)]

    for tamaño,alto in barcosDimensiones:
        colocado=False
        while not colocado:
            horizontal=random.choise([True,False]) #genera la posicion dentro del tablero
            if(horizontal): #genera posicion horizontal
                fila=random.randint(0,tam_tablero-1)
                columna=random.randint(0,tam_tablero-tamaño)
            else:           #genera posicion vertical
                fila=random.randint(0,tam_tablero-tamaño)
                columna=random.randint(0,tam_tablero-1)
            
            #revisar que no se superpongan los barcos
            espacioLleno=False
            for i in range(tamaño):
                if(horizontal):
                    if((fila,columna+i) in barcos):
                        espacioLleno=True
                        break
                else:
                    if((fila+i,columna) in barcos):
                        espacioLleno=True
                        break
            if (not espacioLleno): 
                for i in range(tamaño):
                    if(horizontal):
                        barcos.append((fila,columna+i)) #se guarda la coordenada del barco en la lista
                    else:
                        barcos.append((fila+i,columna))
                colocado=True

    #agregar las imagenes de los barcos repetir esta seccion la cantidad de vecs necesaria para la cantidad de barcos
    for posicion in barcos:
        x=inicioX+posicion[1]*tam_celda
        y=inicioY+posicion[0]*tam_celda
        barcoImagen=pygame.image.load("")
        barcoImagen=pygame.transform.scale(barcoImagen,(tam_celda,tam_celda))
        ventana.blit(barcoImagen,(x,y))


"""






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

    letras="ABCDEFGHIJ" #PRIMERAS 10 LETRAS DE ABECEDARIO
    for columna in range(tam_tablero):
        x=inicioX+columna*tam_celda+tam_celda//2
        y=inicioY-30

        #agregar el texto
        letraEn=letras_Tablero.render(letras[columna],True,negro)
        ventana.blit(letraEn,(x-letraEn.get_width()//2,y))

    numero="12345678910" #PRIMEROS 10 numeros
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


