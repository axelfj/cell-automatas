# Taller de Programación #
# Proyecto 3 #
# Automatas Celulares #
# Axel Fernández Jimenez 2016098894 #
# Maria Jose Paz Gomez 2016106862 #

import pygame, sys
import random
from pygame.locals import *
        
  
# HORMIGA DE LANGTON #

#Automata que utiliza celulas con dos estados. Maneja una posicion dentro de
#la matriz que representa una hormiga que tiene direccion

#Entradas: Automata con celulas en dos estados

#Salidas: Juego de la hormiga de langton en pygame

#Restricciones:
#Si encuentra una celula blanca, gira a la derecha 90 grados, cambia el color
    #de la celula y avanza una celula.
#Si encuentra una celula negra, gira a la izquierda 90 grados, cambia el color
    #de la celula y avanza una celula.
#Si choca con algún límite, la hormiga muere.

 
def mainL(filass,columnass):    
    def dibujarMatriz(M):
        for f in range(filas):
            for c in range(columnas):
                valor = M[f][c]
                if valor == 0:
                    color = (0, 0, 0)
                if valor == 1:
                    color = (255, 255, 255)
                x = margen + c * tamano
                y = margen + f * tamano
                rectangulo = x, y, tamano, tamano
                pygame.draw.rect(screen, color, rectangulo, 0)

           
    def langton(M,fh,ch,hormiga):
        f = fh
        c = ch
        if hormiga == 'norte':
            if M[f][c] == 0:
                fh = f
                ch = c+1
                if ch == len(M[0]):
                    return "La hormiga murió"
                hormiga = "oeste"
                M[f][c] = 1
            else:
                fh= f
                ch = c-1
                if ch<0:
                    return "La hormiga murió"
                hormiga = "este"
                M[f][c] = 0
        elif hormiga == 'oeste':
            if M[f][c] == 0:
                fh = f+1
                ch = c
                if fh == len(M):
                    return "La hormiga se murió"
                hormiga = "sur"
                M[f][c] = 1
            else:
                fh= f-1
                ch = c
                if fh<0:
                    return "La hormiga murió"
                hormiga = "norte"
                M[f][c] = 0
        elif hormiga == 'sur':
            if M[f][c] == 0:
                fh = f
                ch = c-1
                if ch<0:
                    return "La hormiga murió"
                hormiga = "este"
                M[f][c] = 1
            else:
                fh= f
                ch = c+1
                if ch == len(M[0]):
                    return "La hormiga murió"
                hormiga = "oeste"
                M[f][c] = 0
        elif hormiga == 'este':
            if M[f][c] == 0:
                fh = f-1
                ch = c
                if fh<0:
                    return "La hormiga murió"
                hormiga = "norte"
                M[f][c] = 1
            else:
                fh= f+1
                ch = c
                if fh == len(M):
                    return "La hormiga murió"
                hormiga = "sur"
                M[f][c] = 0
        return M,fh,ch,hormiga
    M = [[random.randrange(1,2) for columnas in range(columnass)] for filas in range(filass)]
    tamano = 10     # tamaño de la celda
    margen = 10    # margen con el borde   
    filas = len(M)
    columnas = len(M[0]) 
    anchoVentana = columnas * tamano + 2 * margen
    altoVentana = filas * tamano + 2 * margen

    hormiga = "norte"
    fh = filass//2
    ch = columnass//2
    
    pygame.init()
    screen = pygame.display.set_mode([anchoVentana, altoVentana])
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        M,fh,ch,hormiga = langton(M,fh,ch,hormiga)
        dibujarMatriz(M)
        

