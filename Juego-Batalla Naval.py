import pygame
import sys

pygame.init()

ancho=800
alto=600
azul=(0,0,128)
gris=(150,150,150)
rojo=(255,0,0)
blanco=(255,255,255)
negro=(0,0,0)
verde=(0,255,0)

#configuracion de la ventana -------------------------------------
ventana=pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Batalla Naval - UN") #Nombre de la ventana 

#Fuentes----------------------------------------------------------
pygame.font.init()
Fuente_titulo=pygame.font.Font(None,50) #crecion de la fuente del titulo - none fuente predeterminada- 50 tamaño
Fuente_opcion=pygame.font.Font(None,60)
Fuente_Principal=pygame.font.Font(None,70)

titulo=Fuente_titulo.render("Batalla Naval",True, azul) #renderiza el texto con suavizado

#funcion para dibujar el texto de la pantalla inicial y sus botones
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
        ventana.fill(negro) #limpia la pantalla al inicio de cada iteracion de los bubles, borra lo dibujado anteriormente
        NombreTitulo("BATALLA NAVAL - INTERACTIVO",Fuente_Principal,rojo,ventana,ancho//2,alto//3)
        #Dibujar botones
        BotonJuego=OpcionesMenu("Jugar",Fuente_opcion,azul,gris,ventana,ancho//2-150,alto//2-75,300,100)
        BotonSalir=OpcionesMenu("Salir",Fuente_opcion,verde,gris,ventana,ancho//2-150,alto//2+50,300,100)
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

def JuegoLoop():
    mensaje="Haz click en el area roja"
    run=True
    while run:
        ventana.fill(negro) #limpia la pantalla al inicio de cada iteracion de los bubles, borra lo dibujado anteriormente
        #Eventos-------------------------------------------------------------------------

        for evento in pygame.event.get(): #el pygame.event.get(), genera una lista de los eventos que ocurran dentro de la ventana 
            if(evento.type==pygame.QUIT): #si se cierra la ventana el progrmama lo interpreta cerrando el ciclo while
                run=False
            if(evento.type==pygame.MOUSEBUTTONDOWN): #evento del clic
                x,y=evento.pos #coordenada del clic
                if(100<=x<=300 and 100<=y<=300 ):
                    mensaje ="Clic detactado"


        #Desarrollo juego-------------------------------------------------------------

        #titulo 
        ventana.blit(titulo,(ancho//2 - titulo.get_width()//2,20)) #(texto,(Coordenada x,y))
        pygame.draw.line(ventana,gris,(30,80),(ancho-30,80),2) #(30 valor de ancho, 80 alto), el 2 es el grosor

        #dibujar rectangulo
        pygame.draw.rect(ventana,rojo,(100,100,200,200)) #(x,y,ancho,alto)

        fuente=pygame.font.Font(None,33)
        texto=fuente.render(mensaje, True, blanco)
        ventana.blit(texto,(50,50))

        pygame.display.flip() #refresca la pantalla
    pygame.quit()#Salir del juego 
    sys.exit()#Salir del juego 

#EJECUCION PRINCIPAL
while True:
    modo=MenuPrincipal()
    if(modo=="jugar"):
        JuegoLoop()
