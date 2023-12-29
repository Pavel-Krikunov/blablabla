import random
import pygame
from functoins import load_image


pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))


class Bomb(pygame.sprite.Sprite):
    image1 = load_image("creature.png", colorkey=-1)
    image2 = load_image("bang.png", colorkey=0)

    def __init__(self, pos, *group):
        # Конструктор класса Спрайтов уже осдержит параметр - group который позволяет объединять спрайты в группы
        super().__init__(*group)
        self.image = Bomb.image1
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def bang(self):
        self.image = Bomb.image2
        self.image = pygame.transform.scale(self.image, (50, 50))

    def update(self, clue):
        if clue == 1:
            self.rect = self.rect.move(10, 0)
        if clue == 2:
            self.rect = self.rect.move(0, 10)
        if clue == 3:
            self.rect = self.rect.move(0, -10)
        if clue == 4:
            self.rect = self.rect.move(-10, 0)


if __name__ == '__main__':
    fps = 60
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    running = True
    flag = False
    bomb = Bomb([4, 4], all_sprites)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    bomb.update(1)
                if event.key == pygame.K_DOWN:
                    bomb.update(2)
                if event.key == pygame.K_UP:
                    bomb.update(3)
                if event.key == pygame.K_LEFT:
                    bomb.update(4)
        screen.fill((255, 255, 255))
        if True:
            all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()

    # Подумать,куда воткнуть screen.fill((0, 0, 0))
    # Подумать что поменять, чтобы шарики не уходили за границу экрана(наполовинку уходят)
