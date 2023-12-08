import random

import pygame

from functoins import load_image

pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)


class Bomb(pygame.sprite.Sprite):
    image1 = load_image("bomb.jpg", colorkey=-1)
    image2 = load_image("bang.png")

    def __init__(self, pos, *group):
        # Конструктор класса Спрайтов уже осдержит параметр - group который позволяет объединять спрайты в группы
        super().__init__(*group)
        self.image = Bomb.image1
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def movement(self, pos):
        self.rect.x = event.pos[0]
        self.rect.y = event.pos[1]
        pygame.mouse.set_visible(False)

    def bang(self):
        self.image = Bomb.image2
        self.image = pygame.transform.scale(self.image, (50, 50))

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)


if __name__ == '__main__':
    fps = 60
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    running = True
    bomb1 = Bomb((0, 0), all_sprites)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                bomb1.movement(event.pos)
        screen.fill((0, 0, 0))
        if pygame.mouse.get_focused():
            pygame.mouse.set_visible(False)
            all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()

    # Подумать,куда воткнуть screen.fill((0, 0, 0))
    # Подумать что поменять, чтобы шарики не уходили за границу экрана(наполовинку уходят)
