import pygame
import time
import random

pygame.init()

largura = 900
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake - O Clássico")

#CORES
Verde	= (0, 255, 0)
Roxo	= (128, 0, 128)
Rosa	= (255, 192, 203)
Preto	= (0, 0, 0)
Amarelo	= (255, 255, 0)


#config
tamanho_do_bloco = 20
velocidade = 15


fonte_estilo = pygame.font.SysFont("comicsasms", 40)
