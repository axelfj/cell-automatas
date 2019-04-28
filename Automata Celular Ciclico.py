# Taller de Programación #
# Proyecto 3 #
# Automatas Celulares #
# Axel Fernández Jimenez 2016098894 #
# Maria Jose Paz Gomez 2016106862 #

import pygame, sys
import random
from pygame.locals import *

# AUTOMATA CELULAR CICLICO #

#Se usan 16 estados para las celulas, de 0 a 15. Cada estado es un color
#diferentey que hayan cambios graduales.
#Entradas: Matriz con celulas y 16 estados diferentes
#Salidas: Juego automata celular ciclico en pygame
#Restricciones: Una celula con estado n toma el valor de (n+1)%16 con al
    #menos un vecino con este valor 

def vecinosAutomata(M,f,c):
    vecinos = 0
    actual = M[f][c]
    nex = (actual+1)%16
    if f == 0 and c == 0:
        if M[f][c+1] == nex:
            vecinos +=1
        if M[f+1][c] == nex:
            vecinos +=1
        if M[f+1][c+1] == nex:
            vecinos +=1
        return vecinos
    
    if f == 0 and c == len(M[0])-1:
        if M[f][c-1]== nex:
            vecinos +=1
        if M[f+1][c-1] == nex:
            vecinos +=1
        if M[f+1][c] == nex:
            vecinos +=1
        return vecinos
    
    if f == len(M)-1 and c == 0:
        if M[f-1][c] == nex:
            vecinos +=1
        if M[f-1][c+1] == nex:
            vecinos +=1 
        if M[f][c+1] == nex:
            vecinos +=1 
        return vecinos
    
    if f == len(M)-1 and c == len(M[0])-1:
        if M[f-1][c-1] == nex:
            vecinos +=1
        if M[f-1][c] == nex:
            vecinos +=1
        if M[f][c-1] == nex:
            vecinos +=1
        return vecinos

    if f == 0:
        if M[f][c-1] == nex:
            vecinos +=1
        if M[f][c+1] == nex:
            vecinos +=1
        if M[f+1][c-1] == nex:
            vecinos +=1
        if M[f+1][c] == nex:
            vecinos +=1
        if M[f+1][c+1] == nex:
            vecinos +=1
        return vecinos
    
    if c == 0:
        if M[f-1][c] == nex:
            vecinos +=1
        if M[f-1][c+1] == nex:
            vecinos +=1
        if M[f][c+1] == nex:
            vecinos +=1
        if M[f+1][c] == nex:
            vecinos +=1
        if M[f+1][c+1] == nex:
            vecinos +=1
        return vecinos
    
    if c == len(M[0]) -1:
        if M[f-1][c-1] == nex:
            vecinos +=1
        if M[f-1][c] == nex:
            vecinos +=1
        if M[f][c-1] == nex:
            vecinos +=1
        if M[f+1][c-1] == nex:
            vecinos +=1
        if M[f+1][c]== nex:
            vecinos +=1
        return vecinos
    
    if f == len(M)-1:
        if M[f-1][c-1] == nex:
            vecinos +=1
        if M[f-1][c] == nex:
            vecinos +=1
        if M[f-1][c+1] == nex:
            vecinos +=1
        if M[f][c-1] == nex:
            vecinos +=1
        if M[f][c+1] == nex:
            vecinos +=1
        return vecinos

    
    if M[f-1][c-1] == nex:
        vecinos +=1
    if M[f-1][c] == nex:
        vecinos +=1
    if M[f-1][c+1] == nex:
        vecinos +=1
        
    if M[f][c-1] == nex:
        vecinos +=1
    if M[f+1][c-1] == nex:
        vecinos +=1
    if M[f+1][c] == nex:
        vecinos +=1
    if M[f+1][c+1] == nex:
        vecinos +=1
    
    if M[f][c+1] == nex:
        vecinos +=1    
    
    return vecinos

def mainA(filass,columnass):    
    def dibujarMatriz(M):
        for f in range(len(M)):
            for c in range(len(M[0])):
                valor = M[f][c]
                if valor == 0:
                    color = (255,0,0)
                if valor == 1:
                    color = (255,0,156)
                if valor == 2:
                    color = (230,0,255)
                if valor == 3:
                    color = (166,0,255)
                if valor == 4:
                    color = (102,0,255)
                if valor == 5:
                    color = (21,0,255)
                if valor == 6:
                    color = (0,150,255)
                if valor == 7:
                    color = (0,188,255)
                if valor == 8:
                    color = (0,255,255)
                if valor == 9:
                    color = (0,255,186)
                if valor == 10:
                    color = (0,255,80)
                if valor == 11:
                    color = (0,255,0)
                if valor == 12:
                    color = (100,255,0)
                if valor == 13:
                    color = (200,255,0)
                if valor == 14:
                    color = (255,240,0)
                if valor == 15:
                    color = (255,145,0)
                x = margen + c * tamano
                y = margen + f * tamano
                rectangulo = x, y, tamano, tamano
                pygame.draw.rect(screen, color, rectangulo, 0)
                
    def automata(M):
        nuevaM = []

        for f in range(len(M)):
            new = []
            for c in range(len(M[0])):
                people = vecinosAutomata(M,f,c)
                if people >= 1:
                    new += [(M[f][c]+1)%16]
                else:
                    new += [M[f][c]]
            nuevaM += [new]
        return nuevaM
        
    M = [[random.randrange(16) for columnas in range(columnass)] for filas in range(filass)]
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
        M = automata(M)
        dibujarMatriz(M)
