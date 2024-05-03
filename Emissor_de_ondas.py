import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Controle do framerate
fps = 120
clock = pygame.time.Clock()

# Configurações iniciais
tamanhoCanva = 600
c = 4
t = 0
dt = 1

# Cores
COR_FUNDO = (20, 20, 20)
COR_CIRCULO = (200, 100, 220)

# Configurações da janela
tela = pygame.display.set_mode((tamanhoCanva, tamanhoCanva))
pygame.display.set_caption('Propagação de onda')

class Circulo:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t
        self.raio = 0
        self.x0 = x
        self.y0 = y
        self.aSerRemovido = False

    def checar_tempo(self):
        if self.raio > 1.6 * tamanhoCanva:
            self.aSerRemovido = True

    def propaga_campo(self):
        self.raio += c * dt

    def mostra(self):
        pygame.draw.circle(tela, COR_CIRCULO, (int(self.x), int(self.y)), int(self.raio), width=1)

def emiteCampo(x, y):
    novo_circulo = Circulo(x, y, t)
    circulos.append(novo_circulo)    

# Lista para armazenar os círculos
circulos = []

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            emiteCampo(*pygame.mouse.get_pos())

    emiteCampo(*pygame.mouse.get_pos())

    tela.fill(COR_FUNDO)

    for i in range(len(circulos) - 1, -1, -1):
        circulo = circulos[i]
        circulo.propaga_campo()
        circulo.mostra()
        circulo.checar_tempo()

        if circulo.aSerRemovido:
            circulos.pop(i)

        t += dt

    fonte = pygame.font.Font(None, 18)
    texto = fonte.render("nicolasheringer@ufmg.br", True, (255,255,255))
    tela.blit(texto, (tamanhoCanva-160, tamanhoCanva-20))

    pygame.display.flip()

    clock.tick(fps)
