import pygame
import time
import random

pygame.init()

largura = 900
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake - O Clássico")

#CORES
verde	= (0, 255, 0)
roxo	= (128, 0, 128)
rosa	= (255, 192, 203)
preto	= (0, 0, 0)
amarelo	= (255, 255, 0)


#config
tamanho_do_bloco = 20
velocidade = 15


fonte_estilo = pygame.font.SysFont("comicsasms", 40)
fonte_pontuacao = pygame.font.SysFont("comicsanms", 25)

def mensagem (msg, cor):
    texto = fonte_estilo.render(msg, True, cor)
    tela.blit(texto, [largura / 6, altura / 3])


def sua_pontuacao(pontos):
    valor = fonte_pontuacao.render("Pontuações: " + str(pontos), True,  amarelo)
    tela.blit(valor, [10, 10])


def jogo():
    sair_do_jogo = False
    fim_jogo = False

x1 = largura / 2
y1 = altura / 2

x1_troca = 0
y1_troca = 0

corpo_cobra = []
comprimento_cobra = 1

