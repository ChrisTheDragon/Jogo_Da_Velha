import pygame

pygame.init()

# CORES PADRÃO
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (198, 25, 8)
indigo = (75, 0, 130)
purpura = (128, 0, 128)
darkMagenta = (139, 0, 139)
magenta = (255, 0, 255)
violeta = (238, 130, 238)
roxo = (94, 0, 135)

# CORES STRANGER THINGS
st_preto = (0, 0, 0)
st_vermelho = (198, 25, 8)
st_azul = (29, 76, 106)
st_amarelo = (99, 50, 7)
st_cinzaesc = (36, 44, 29)
st_cinzaazul = (58, 90, 115)
st_roxocla = (101, 57, 80)
st_roxoesc = (81, 44, 62)

# TELA
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
tela.fill(branco)
pygame.display.set_caption('Jogo da Velha')

# MUSICA
som_vitoria = pygame.mixer.Sound('Sons/vitoria_1.wav')
som_vitoria_2 = pygame.mixer.Sound('Sons/vitoria_2.mp3')
som_empate = pygame.mixer.Sound('Sons/empate_1.wav')
som_empate.set_volume(0.1)

# IMAGENS
# -> Placar
X_pd_placar = pygame.image.load('Imagens/X_padrão.png')
X_pd_placar_r = pygame.transform.scale(X_pd_placar, (45, 45))
O_pd_placar = pygame.image.load('Imagens/O_padrão.png')
O_pd_placar_r = pygame.transform.scale(O_pd_placar, (45, 45))

X_1_placar = pygame.image.load('Imagens/X1.png').convert_alpha()
X_1_placar_r = pygame.transform.scale(X_1_placar, (45, 45))
O_1_placar = pygame.image.load('Imagens/O1.png').convert_alpha()
O_1_placar_r = pygame.transform.scale(O_1_placar, (45, 45))

X_2_placar = pygame.image.load('Imagens/X2.png').convert_alpha()
X_2_placar_r = pygame.transform.scale(X_2_placar, (45, 45))
O_2_placar = pygame.image.load('Imagens/O2.png').convert_alpha()
O_2_placar_r = pygame.transform.scale(O_2_placar, (45, 45))

# ->Peças
X_pd_peca = pygame.image.load('Imagens/X_padrão.png').convert_alpha()
X_pd_peca_r = pygame.transform.scale(X_pd_peca, (160, 160))
O_pd_peca = pygame.image.load('Imagens/O_padrão.png').convert_alpha()
O_pd_peca_r = pygame.transform.scale(O_pd_peca, (160, 160))

X_1_peca = pygame.image.load('Imagens/X1.png').convert_alpha()
X_1_peca_r = pygame.transform.scale(X_1_peca, (160, 160))
O_1_peca = pygame.image.load('Imagens/O1.png').convert_alpha()
O_1_peca_r = pygame.transform.scale(O_1_peca, (160, 160))

X_2_peca = pygame.image.load('Imagens/X2.png').convert_alpha()
X_2_peca_r = pygame.transform.scale(X_2_peca, (160, 160))
O_2_peca = pygame.image.load('Imagens/O2.png').convert_alpha()
O_2_peca_r = pygame.transform.scale(O_2_peca, (160, 160))

Img_lateral = pygame.image.load('Imagens/Barra Lateral.png').convert_alpha()
Img_lateral_r = pygame.transform.scale(Img_lateral, (160, 480))
