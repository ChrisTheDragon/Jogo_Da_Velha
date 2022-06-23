import pygame
from pygame.locals import *
from sys import exit
import Essenciais as ex

pygame.init()

# VARIAVEIS GOBLAIS
ESTADO = 'JOGANDO'
VEZ = 'JOG1'
ESCOLHA = 'X'
JOGADAS = 0
LINHAVIT = 0
PONTOSX = 0
PONTOSO = 0
DIFICULDADE = 0

# TELA
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
tela.fill(ex.branco)
pygame.display.set_caption('Jogo da Velha')

# FONTE
fonte1 = pygame.font.SysFont('Comic Sans MS', 40)
fonte2 = pygame.font.SysFont('Comic Sans MS', 15)
fonte3 = pygame.font.SysFont('Comic Sans MS', 45)
fonte4 = pygame.font.SysFont('Times New Roman', 15)

# MUSICA
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.load('Sons/background_music_2.mp3')
pygame.mixer.music.play(-1)

# TABULEIRO
if DIFICULDADE == 0:
    tabuleiro = [1, 2, 3,
                 4, 5, 6,
                 7, 8, 9]
elif DIFICULDADE == 1:
    tabuleiro = [1, 2, 3, 4,
                 5, 6, 7, 8,
                 9, 10, 11, 12,
                 13, 14, 15, 16]

# CÉLULAS
quadrado1_9 = pygame.draw.rect(tela, ex.preto, (0, 0, 160, 160))
quadrado2_9 = pygame.draw.rect(tela, ex.preto, (160, 0, 160, 160))
quadrado3_9 = pygame.draw.rect(tela, ex.preto, (320, 0, 160, 160))
quadrado4_9 = pygame.draw.rect(tela, ex.preto, (0, 160, 160, 160))
quadrado5_9 = pygame.draw.rect(tela, ex.preto, (160, 160, 160, 160))
quadrado6_9 = pygame.draw.rect(tela, ex.preto, (320, 160, 160, 160))
quadrado7_9 = pygame.draw.rect(tela, ex.preto, (0, 320, 160, 160))
quadrado8_9 = pygame.draw.rect(tela, ex.preto, (160, 320, 160, 160))
quadrado9_9 = pygame.draw.rect(tela, ex.preto, (320, 320, 160, 160))
celulas9 = [
    quadrado1_9, quadrado2_9, quadrado3_9,
    quadrado4_9, quadrado5_9, quadrado6_9,
    quadrado7_9, quadrado8_9, quadrado9_9
]

quadrado1 = pygame.draw.rect(tela, ex.preto, (0, 0, 120, 120))
quadrado2 = pygame.draw.rect(tela, ex.preto, (120, 0, 120, 120))
quadrado3 = pygame.draw.rect(tela, ex.preto, (240, 0, 120, 120))
quadrado4 = pygame.draw.rect(tela, ex.preto, (360, 0, 120, 120))
quadrado5 = pygame.draw.rect(tela, ex.preto, (0, 120, 120, 120))
quadrado6 = pygame.draw.rect(tela, ex.preto, (120, 120, 120, 120))
quadrado7 = pygame.draw.rect(tela, ex.preto, (240, 120, 120, 120))
quadrado8 = pygame.draw.rect(tela, ex.preto, (360, 120, 120, 120))
quadrado9 = pygame.draw.rect(tela, ex.preto, (0, 240, 120, 120))
quadrado10 = pygame.draw.rect(tela, ex.preto, (120, 240, 120, 120))
quadrado11 = pygame.draw.rect(tela, ex.preto, (240, 240, 120, 120))
quadrado12 = pygame.draw.rect(tela, ex.preto, (360, 240, 120, 120))
quadrado13 = pygame.draw.rect(tela, ex.preto, (0, 360, 120, 120))
quadrado14 = pygame.draw.rect(tela, ex.preto, (120, 360, 120, 120))
quadrado15 = pygame.draw.rect(tela, ex.preto, (240, 360, 120, 120))
quadrado16 = pygame.draw.rect(tela, ex.preto, (360, 360, 120, 120))
celulas16 = [
    quadrado1, quadrado2, quadrado3, quadrado4,
    quadrado5, quadrado6, quadrado7, quadrado8,
    quadrado9, quadrado10, quadrado11, quadrado12,
    quadrado13, quadrado14, quadrado15, quadrado16
]


def janela(tela):
    global DIFICULDADE
    # Imprime o tabuleiro
    if DIFICULDADE == 0:
        pygame.draw.line(tela, ex.vermelho, (160, 0), (160, 640), 10)
        pygame.draw.line(tela, ex.vermelho, (320, 0), (320, 640), 10)
        pygame.draw.line(tela, ex.vermelho, (0, 160), (480, 160), 10)
        pygame.draw.line(tela, ex.vermelho, (0, 320), (480, 320), 10)
        pygame.draw.rect(tela, ex.purpura, (480, 0, 160, 640))
    elif DIFICULDADE == 1:
        pygame.draw.line(tela, ex.vermelho, (120, 0), (120, 640), 10)
        pygame.draw.line(tela, ex.vermelho, (240, 0), (240, 640), 10)
        pygame.draw.line(tela, ex.vermelho, (360, 0), (360, 640), 10)
        pygame.draw.line(tela, ex.vermelho, (0, 120), (480, 120), 10)
        pygame.draw.line(tela, ex.vermelho, (0, 240), (480, 240), 10)
        pygame.draw.line(tela, ex.vermelho, (0, 360), (480, 360), 10)

    tela.blit(ex.Img_lateral_r, (480, 0))  # Barra Lateral
    pygame.draw.rect(tela, ex.preto, (485, 90, 160, 110))
    tela.blit(ex.O_2_placar_r, (485, 100))  # Placar O
    tela.blit(ex.X_2_placar_r, (485, 150))  # Placar X

    mens1 = 'Feito por:'
    mens2 = 'Christian Marinho'
    mens3 = '&'
    mens4 = 'Leticia Costa'
    texto1 = fonte4.render(mens1, True, ex.branco)
    texto2 = fonte4.render(mens2, True, ex.branco)
    texto3 = fonte4.render(mens3, True, ex.branco)
    texto4 = fonte4.render(mens4, True, ex.branco)
    tela.blit(texto1, (530, 410))
    tela.blit(texto2, (500, 425))
    tela.blit(texto3, (550, 440))
    tela.blit(texto4, (515, 455))


def imp_peca(pos):
    # Imprime X ou O
    global VEZ, DIFICULDADE
    x, y = pos
    if VEZ == 'JOG2':  # Se a vez for do Jogador 2
        if DIFICULDADE == 1:
            O_2_peca_r = pygame.transform.scale(ex.O_2_peca, (120, 120))
        else:
            O_2_peca_r = pygame.transform.scale(ex.O_2_peca, (160, 160))
        tela.blit(O_2_peca_r, (x, y))
    else:  # Se a vez for do jogador 1
        if DIFICULDADE == 1:
            X_2_peca_r = pygame.transform.scale(ex.X_2_peca, (120, 120))
        else:
            X_2_peca_r = pygame.transform.scale(ex.X_2_peca, (160, 160))
        tela.blit(X_2_peca_r, (x, y))


def teste_botao9():
    # testa aonde o mouse clicou
    for p in celulas9:
        if event.type == MOUSEBUTTONDOWN and p.collidepoint(posi_mouse):  # Se houver um click e na posição do mouse
            if p == quadrado1_9:  # verifica qual foi o quadrado clicado
                jogada(0, [0, 0])
            if p == quadrado2_9:
                jogada(1, [160, 0])
            if p == quadrado3_9:
                jogada(2, [320, 0])
            if p == quadrado4_9:
                jogada(3, [0, 160])
            if p == quadrado5_9:
                jogada(4, [160, 160])
            if p == quadrado6_9:
                jogada(5, [320, 160])
            if p == quadrado7_9:
                jogada(6, [0, 320])
            if p == quadrado8_9:
                jogada(7, [160, 320])
            if p == quadrado9_9:
                jogada(8, [320, 320])


def teste_botao16():
    for p in celulas16:
        if event.type == MOUSEBUTTONDOWN and p.collidepoint(posi_mouse):
            if p == quadrado1:
                jogada(0, [0, 0])
            if p == quadrado2:
                jogada(1, [120, 0])
            if p == quadrado3:
                jogada(2, [240, 0])
            if p == quadrado4:
                jogada(3, [360, 0])
            if p == quadrado5:
                jogada(4, [0, 120])
            if p == quadrado6:
                jogada(5, [120, 120])
            if p == quadrado7:
                jogada(6, [240, 120])
            if p == quadrado8:
                jogada(7, [360, 120])
            if p == quadrado9:
                jogada(8, [0, 240])
            if p == quadrado10:
                jogada(9, [120, 240])
            if p == quadrado11:
                jogada(10, [240, 240])
            if p == quadrado12:
                jogada(11, [360, 240])
            if p == quadrado13:
                jogada(12, [0, 360])
            if p == quadrado14:
                jogada(13, [120, 360])
            if p == quadrado15:
                jogada(14, [240, 360])
            if p == quadrado16:
                jogada(15, [360, 360])


def jogada(ind, pos):
    # Faz uma jogada e muda para o oponete
    global ESCOLHA, VEZ, JOGADAS
    if tabuleiro[ind] == 'X':  # Se o click foi em uma celula que ja esta marcada, não faz nada
        pass
    elif tabuleiro[ind] == 'O':
        pass
    else:  # se o click foi em uma celula vazia, marca a celula e muda a vez pro oponente
        tabuleiro[ind] = ESCOLHA
        imp_peca(pos)  # imprime na posição marcada
        if VEZ == 'JOG1':
            VEZ = 'JOG2'
        else:
            VEZ = 'JOG1'
        JOGADAS += 1


def vitoria(jog):
    global LINHAVIT, DIFICULDADE
    # Testa se um jogador venceu
    if DIFICULDADE == 0:
        if tabuleiro[0] == jog and tabuleiro[1] == jog and tabuleiro[2] == jog:
            LINHAVIT = 1
            return True
        if tabuleiro[3] == jog and tabuleiro[4] == jog and tabuleiro[5] == jog:
            LINHAVIT = 2
            return True
        if tabuleiro[6] == jog and tabuleiro[7] == jog and tabuleiro[8] == jog:
            LINHAVIT = 3
            return True
        if tabuleiro[0] == jog and tabuleiro[4] == jog and tabuleiro[8] == jog:
            LINHAVIT = 4
            return True
        if tabuleiro[2] == jog and tabuleiro[4] == jog and tabuleiro[6] == jog:
            LINHAVIT = 5
            return True
        if tabuleiro[0] == jog and tabuleiro[3] == jog and tabuleiro[6] == jog:
            LINHAVIT = 6
            return True
        if tabuleiro[1] == jog and tabuleiro[4] == jog and tabuleiro[7] == jog:
            LINHAVIT = 7
            return True
        if tabuleiro[2] == jog and tabuleiro[5] == jog and tabuleiro[8] == jog:
            LINHAVIT = 8
            return True
    elif DIFICULDADE == 1:
        if tabuleiro[0] == jog and tabuleiro[1] == jog and tabuleiro[2] == jog and tabuleiro[3] == jog:
            LINHAVIT = 9
            return True
        if tabuleiro[4] == jog and tabuleiro[5] == jog and tabuleiro[6] == jog and tabuleiro[7] == jog:
            LINHAVIT = 10
            return True
        if tabuleiro[8] == jog and tabuleiro[9] == jog and tabuleiro[10] == jog and tabuleiro[11] == jog:
            LINHAVIT = 11
            return True
        if tabuleiro[12] == jog and tabuleiro[13] == jog and tabuleiro[14] == jog and tabuleiro[15] == jog:
            LINHAVIT = 12
            return True
        if tabuleiro[0] == jog and tabuleiro[5] == jog and tabuleiro[10] == jog and tabuleiro[15] == jog:
            LINHAVIT = 4
            return True
        if tabuleiro[3] == jog and tabuleiro[6] == jog and tabuleiro[9] == jog and tabuleiro[12] == jog:
            LINHAVIT = 5
            return True
        if tabuleiro[0] == jog and tabuleiro[4] == jog and tabuleiro[8] == jog and tabuleiro[12] == jog:
            LINHAVIT = 13
            return True
        if tabuleiro[1] == jog and tabuleiro[5] == jog and tabuleiro[9] == jog and tabuleiro[13] == jog:
            LINHAVIT = 14
            return True
        if tabuleiro[2] == jog and tabuleiro[6] == jog and tabuleiro[10] == jog and tabuleiro[14] == jog:
            LINHAVIT = 15
            return True
        if tabuleiro[3] == jog and tabuleiro[7] == jog and tabuleiro[11] == jog and tabuleiro[15] == jog:
            LINHAVIT = 16
            return True

def texto_vitoria(vit):
    if vit == 'EMPATE':
        menssagem = 'NINGUEM VENÇEU'
        texto = fonte1.render(menssagem, True, ex.branco)
        tela.blit(texto, (100, 200))
        ex.som_empate.play()  # som de empate
    else:
        menssagem = 'Jogador {} venceu!'.format(vit)
        texto = fonte1.render(menssagem, True, ex.branco)
        tela.blit(texto, (100, 200))
        ex.som_vitoria_2.play()  # som de vitória


def linha_vitoria(tela):
    a, b, c, d = 0, 0, 0, 0
    if LINHAVIT == 1:
        a = 20
        b = 80
        c = 460
        d = 80
    elif LINHAVIT == 2:
        a = 20
        b = 240
        c = 460
        d = 240
    elif LINHAVIT == 3:
        a = 20
        b = 400
        c = 460
        d = 400
    elif LINHAVIT == 4:
        a = 10
        b = 10
        c = 470
        d = 470
    elif LINHAVIT == 5:
        a = 10
        b = 470
        c = 470
        d = 10
    elif LINHAVIT == 6:
        a = 80
        b = 10
        c = 80
        d = 470
    elif LINHAVIT == 7:
        a = 240
        b = 10
        c = 240
        d = 470
    elif LINHAVIT == 8:
        a = 400
        b = 10
        c = 400
        d = 470
    elif LINHAVIT == 9:
        a = 20
        b = 60
        c = 460
        d = 60
    elif LINHAVIT == 10:
        a = 20
        b = 180
        c = 460
        d = 180
    if LINHAVIT == 11:
        a = 20
        b = 300
        c = 460
        d = 300
    if LINHAVIT == 12:
        a = 20
        b = 420
        c = 460
        d = 420
    if LINHAVIT == 13:
        a = 60
        b = 10
        c = 60
        d = 470
    if LINHAVIT == 14:
        a = 180
        b = 10
        c = 180
        d = 470
    if LINHAVIT == 15:
        a = 300
        b = 10
        c = 300
        d = 470
    if LINHAVIT == 16:
        a = 420
        b = 10
        c = 420
        d = 470

    pygame.draw.line(tela, ex.roxo, (a, b), (c, d), 10)


def botao_reset():
    # Desenta o botão de reset
    global PONTOSO, PONTOSX
    pygame.draw.rect(tela, ex.st_preto, (510, 20, 100, 35))
    b_resete = fonte2.render('RECOMEÇAR', True, ex.vermelho)  # Botão de Reset
    tela.blit(b_resete, (515, 25))
    if event.type == MOUSEBUTTONDOWN and 510 <= posi_mouse[0] <= 610 and 20 <= posi_mouse[1] <= 55:
        resete()
        PONTOSO, PONTOSX = 0, 0


def botao_dificuldade():
    global DIFICULDADE, PONTOSX, PONTOSO
    # desenha o botão de dificuldade
    pygame.draw.rect(tela, ex.preto, (490, 220, 60, 50))
    tela.blit(ex.dific_0_r, (493, 219))
    pygame.draw.rect(tela, ex.preto, (570, 220, 60, 50))
    tela.blit(ex.dific_1_r, (575, 219))
    if event.type == MOUSEBUTTONDOWN and 490 <= posi_mouse[0] <= 550 and 220 <= posi_mouse[1] <= 270:
        if DIFICULDADE == 1:
            PONTOSO, PONTOSX = 0, 0
        DIFICULDADE = 0
        resete()
    if event.type == MOUSEBUTTONDOWN and 570 <= posi_mouse[0] <= 630 and 220 <= posi_mouse[1] <= 270:
        if DIFICULDADE == 0:
            PONTOSO, PONTOSX = 0, 0
        DIFICULDADE = 1
        resete()


def resete():
    # Reseta o jogo inteiro
    global ESTADO, VEZ, ESCOLHA, JOGADAS, LINHAVIT, tabuleiro, DIFICULDADE
    ESTADO = 'JOGANDO'
    VEZ = 'JOG1'
    ESCOLHA = 'X'
    JOGADAS = 0
    LINHAVIT = 0
    if DIFICULDADE == 0:
        tabuleiro = [1, 2, 3,
                     4, 5, 6,
                     7, 8, 9]
    elif DIFICULDADE == 1:
        tabuleiro = [1, 2, 3, 4,
                     5, 6, 7, 8,
                     9, 10, 11, 12,
                     13, 14, 15, 16]
    tela.fill(ex.preto)


while True:
    posi_mouse = pygame.mouse.get_pos()  # Guarda a posição do cursor do mouse
    if ESTADO == 'JOGANDO':
        for event in pygame.event.get():
            # FECHA TELA
            if event.type == QUIT:
                pygame.quit()
                exit()
            # JOGADA
            if event.type == MOUSEBUTTONDOWN:
                if VEZ == 'JOG1':
                    ESCOLHA = 'X'  # Jogador 1 é X
                    if DIFICULDADE == 0:
                        teste_botao9()  # Se houver um click, verifica aonde foi o click na tela
                    else:
                        teste_botao16()
                else:
                    ESCOLHA = 'O'  # Jogador 2 é O
                    if DIFICULDADE == 0:
                        teste_botao9()
                    else:
                        teste_botao16()
        # JOGO
        janela(tela)  # Cria Janela
        botao_reset()  # Cria e testa o botão reste
        botao_dificuldade() #Cria e testa o botão de dificuldade

        # Testa a vitória
        if vitoria('X'):
            linha_vitoria(tela)
            texto_vitoria('X')
            PONTOSX += 1
            ESTADO = 'RESET'
        elif vitoria('O'):
            linha_vitoria(tela)
            texto_vitoria('O')
            ESTADO = 'RESET'
            PONTOSO += 1
        elif JOGADAS >= 9 and DIFICULDADE == 0 or JOGADAS >= 16 and DIFICULDADE == 1:
            texto_vitoria('EMPATE')
            ESTADO = 'RESET'

        # Cria o Placar
        pontX = fonte3.render(str(PONTOSX), True, ex.branco)
        tela.blit(pontX, (540, 141))
        pontO = fonte3.render(str(PONTOSO), True, ex.branco)
        tela.blit(pontO, (540, 87))

    else:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                resete()
                janela(tela)

    pygame.display.update()
