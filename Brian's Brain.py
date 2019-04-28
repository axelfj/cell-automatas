# Taller de Programación #
# Proyecto 3 #
# Automatas Celulares #
# Axel Fernández Jimenez 2016098894 #
# Maria Jose Paz Gomez 2016106862 #

import pygame, sys
import random
from pygame.locals import *

## EL CEREBRO DE BRIAN ##

# Celulas en tres estados diferentes: viva, muriendo o muerta.
# Cada una de ellas tiene 8 vecinos diferentes

#Entradas: Matriz M con tres celulas diferentes en distintos estados

#Salidas: Juego del cerebro de Brian en pygame

#Restricciones:
#Si una celula muerta tiene 2 vecinos vivos, se convierte en celula viva
#La celula viva siempre se convierte en celula que esta muriendo, no importan
    #los vecinos
#La celula que esta muriendo siempre se convierte en celula muerta, no
    #importan los vecinos

def vecinosBrian(M,f,c):
    vecinos = 0
    
    if f == 0 and c == 0:
        if M[f][c+1] == 2:
            vecinos +=1
        if M[f+1][c] == 2:
            vecinos +=1
        if M[f+1][c+1] == 2:
            vecinos +=1
        return vecinos
    
    if f == 0 and c == len(M[0])-1:
        if M[f][c-1]== 2:
            vecinos +=1
        if M[f+1][c-1] == 2:
            vecinos +=1
        if M[f+1][c] == 2:
            vecinos +=1
        return vecinos
    
    if f == len(M)-1 and c == 0:
        if M[f-1][c] == 2:
            vecinos +=1
        if M[f-1][c+1] == 2:
            vecinos +=1 
        if M[f][c+1] == 2:
            vecinos +=1 
        return vecinos
    
    if f == len(M)-1 and c == len(M[0])-1:
        if M[f-1][c-1] == 2:
            vecinos +=1
        if M[f-1][c] == 2:
            vecinos +=1
        if M[f][c-1] == 2:
            vecinos +=1
        return vecinos

    if f == 0:
        if M[f][c-1] == 2:
            vecinos +=1
        if M[f][c+1] == 2:
            vecinos +=1
        if M[f+1][c-1] == 2:
            vecinos +=1
        if M[f+1][c] == 2:
            vecinos +=1
        if M[f+1][c+1] == 2:
            vecinos +=1
        return vecinos
    
    if c == 0:
        if M[f-1][c] == 2:
            vecinos +=1
        if M[f-1][c+1] == 2:
            vecinos +=1
        if M[f][c+1] == 2:
            vecinos +=1
        if M[f+1][c] == 2:
            vecinos +=1
        if M[f+1][c+1] == 2:
            vecinos +=1
        return vecinos
    
    if c == len(M[0]) -1:
        if M[f-1][c-1] == 2:
            vecinos +=1
        if M[f-1][c] == 2:
            vecinos +=1
        if M[f][c-1] == 2:
            vecinos +=1
        if M[f+1][c-1] == 2:
            vecinos +=1
        if M[f+1][c]== 2:
            vecinos +=1
        return vecinos
    
    if f == len(M)-1:
        if M[f-1][c-1] == 2:
            vecinos +=1
        if M[f-1][c] == 2:
            vecinos +=1
        if M[f-1][c+1] == 2:
            vecinos +=1
        if M[f][c-1] == 2:
            vecinos +=1
        if M[f][c+1] == 2:
            vecinos +=1
        return vecinos

    
    if M[f-1][c-1] == 2:
        vecinos +=1
    if M[f-1][c] == 2:
        vecinos +=1
    if M[f-1][c+1] == 2:
        vecinos +=1
        
    if M[f][c-1] == 2:
        vecinos +=1
    if M[f+1][c-1] == 2:
        vecinos +=1
    if M[f+1][c] == 2:
        vecinos +=1
    if M[f+1][c+1] == 2:
        vecinos +=1
    
    if M[f][c+1] == 2:
        vecinos +=1    
    
    return vecinos

def mainB(filass,columnass):    
    def dibujarMatriz(M):
        for f in range(len(M)):
            for c in range(len(M[0])):
                valor = M[f][c]
                if valor == 0:
                    color = (0, 0, 0)
                if valor == 1:
                    color = (255,0,0)
                if valor == 2:
                    color = (255, 255, 255)
                x = margen + c * tamano
                y = margen + f * tamano
                rectangulo = x, y, tamano, tamano
                pygame.draw.rect(screen, color, rectangulo, 0)
    def brian(M):
        nuevaM = []

        for f in range(len(M)):
            new = []
            for c in range(len(M[0])):
                people = vecinosBrian(M,f,c)
                if M[f][c] == 2:
                    new += [1]
                if M[f][c] == 1:
                    new += [0]
                if M[f][c] == 0:
                    if people == 2:
                        new+= [2]
                    else:
                        new+= [0]
            nuevaM += [new]
        return nuevaM
        
    M = [[random.randrange(3) for columnas in range(columnass)] for filas in range(filass)]
    tamano = 10     # tamaño de la celda
    margen = 10     # margen con el borde   
    filas = len(M)
    columnas = len(M[0]) 
    anchoVentana = columnas * tamano + 2 * margen
    altoVentana = filas * tamano + 2 * margen
    pygame.init()
    screen = pygame.display.set_mode([anchoVentana, altoVentana])
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        M = brian(M)
        dibujarMatriz(M)
