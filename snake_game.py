import pygame
import random

pygame.init()

largura = 900
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake - O Clássico")

# CORES
verde = (0, 255, 0)
roxo = (128, 0, 128)
rosa = (255, 192, 203)
preto = (0, 0, 0)
amarelo = (255, 255, 0)

# config
tamanho_do_bloco = 20
velocidade = 15

# Fontes -
fonte_estilo = pygame.font.SysFont("comicsansms", 40)
fonte_pontuacao = pygame.font.SysFont("comicsansms", 25)
fonte_gameover = pygame.font.SysFont("comicsansms", 30)  

def mensagem(msg, cor, fonte):
    texto = fonte.render(msg, True, cor)
    texto_rect = texto.get_rect(center=(largura/2, altura/3))
    tela.blit(texto, texto_rect)

def sua_pontuacao(pontos):
    valor = fonte_pontuacao.render("Pontuações: " + str(pontos), True, amarelo)
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

    comida_x = round(random.randrange(0, largura - tamanho_do_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_do_bloco) / 20.0) * 20.0

    relogio = pygame.time.Clock()

    while not sair_do_jogo:
        while fim_jogo:
            tela.fill(preto)
            mensagem("Você perdeu! Pressione Q para sair ou C para continuar", roxo, fonte_gameover)
            sua_pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sair_do_jogo = True
                    fim_jogo = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        sair_do_jogo = True
                        fim_jogo = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair_do_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x1_troca == 0:
                    x1_troca = -tamanho_do_bloco
                    y1_troca = 0
                elif evento.key == pygame.K_RIGHT and x1_troca == 0:
                    x1_troca = tamanho_do_bloco
                    y1_troca = 0
                elif evento.key == pygame.K_UP and y1_troca == 0:
                    y1_troca = -tamanho_do_bloco
                    x1_troca = 0
                elif evento.key == pygame.K_DOWN and y1_troca == 0:
                    y1_troca = tamanho_do_bloco
                    x1_troca = 0

        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            fim_jogo = True

        x1 += x1_troca
        y1 += y1_troca
        tela.fill(preto)
        pygame.draw.rect(tela, rosa, [comida_x, comida_y, tamanho_do_bloco, tamanho_do_bloco])
        
        cabeca_cobra = [x1, y1]
        corpo_cobra.append(cabeca_cobra)
        
        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]

        for bloco in corpo_cobra[:-1]:
            if bloco == cabeca_cobra:
                fim_jogo = True

        for bloco in corpo_cobra:
            pygame.draw.rect(tela, verde, [bloco[0], bloco[1], tamanho_do_bloco, tamanho_do_bloco])

        sua_pontuacao(comprimento_cobra - 1)
        pygame.display.update()

        cabeca_rect = pygame.Rect(x1, y1, tamanho_do_bloco, tamanho_do_bloco)
        comida_rect = pygame.Rect(comida_x, comida_y, tamanho_do_bloco, tamanho_do_bloco)

        if cabeca_rect.colliderect(comida_rect):
            comida_x = round(random.randrange(0, largura - tamanho_do_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_do_bloco) / 20.0) * 20.0
            comprimento_cobra += 1

        relogio.tick(velocidade)

    pygame.quit()
    quit()

jogo()