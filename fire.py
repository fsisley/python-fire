import sys
import pygame
import random
from random import randrange
pygame.init()


class Fogo:
    def __init__(self, largura, altura, tamanho_pixel):
        self.largura = largura
        self.altura = altura
        self.largura_virtual = int(largura/tamanho_pixel)
        self.altura_virtual = int(altura/tamanho_pixel)
        self.tamanho_pixel = tamanho_pixel
        ultima_linha = [36]*int(self.largura/self.tamanho_pixel)
        self.dados = [0]*int(self.largura/self.tamanho_pixel *
                             (self.altura/self.tamanho_pixel-1))
        self.dados = self.dados+ultima_linha

    def pinta(self, screen):
        for index, pixel in enumerate(self.dados):
            pygame.draw.rect(screen, cores_fogo[pixel],
                             pygame.Rect((index % self.largura_virtual)*self.tamanho_pixel, (index // self.largura_virtual)*self.tamanho_pixel, self.tamanho_pixel, self.tamanho_pixel))

    def propaga(self):
        for index, pixel in enumerate(self.dados):
            posicao_baixo = index+self.largura_virtual
            if posicao_baixo < len(self.dados):
                valor_baixo = self.dados[posicao_baixo]
                vento = random.randrange(0, 3)
                self.dados[max(index-vento, 0)] = max(valor_baixo-vento, 0)


cores_fogo = [
    (7,   7,  7),
    (31,  7,  7),
    (47,  15, 7),
    (71,  15, 7),
    (87,  23, 7),
    (103, 31, 7),
    (119, 31, 7),
    (143, 39, 7),
    (159, 47, 7),
    (175, 63, 7),
    (191, 71, 7),
    (199, 71, 7),
    (223, 79, 7),
    (223, 87, 7),
    (223, 87, 7),
    (215, 95, 7),
    (215, 95, 7),
    (215, 103, 15),
    (207, 111, 15),
    (207, 119, 15),
    (207, 127, 15),
    (207, 135, 23),
    (199, 135, 23),
    (199, 143, 23),
    (199, 151, 31),
    (191, 159, 31),
    (191, 159, 31),
    (191, 167, 39),
    (191, 167, 39),
    (191, 175, 47),
    (183, 175, 47),
    (183, 183, 47),
    (183, 183, 55),
    (207, 207, 111),
    (223, 223, 159),
    (239, 239, 199),
    (255, 255, 255)
]

size = width, height = 800, 600

screen = pygame.display.set_mode(size)

fogo_no_cu = Fogo(width, height, 3)

movimento = 0
fps = pygame.time.Clock()


def limpa_tela():
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((0, 0), size))


while True:
    fps.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == 270 or event.key == 61:
                fogo_no_cu = Fogo(width, height, fogo_no_cu.tamanho_pixel+1)
            if event.key == 269 or event.key == 45:
                fogo_no_cu = Fogo(width, height, fogo_no_cu.tamanho_pixel-1)
            if event.key == 27:
                sys.exit()

    limpa_tela()
    fogo_no_cu.propaga()
    fogo_no_cu.pinta(screen)
    # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
    #     150+movimento, 100+movimento, 50, 70), 2)
    # movimento = movimento+1
    # pygame.draw.circle(screen, (100, 150, 200),
    #                    (50, 50), int(20+movimento*1.55))

    pygame.display.flip()
