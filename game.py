import sys

import pygame

s_width = 640
s_hight = 480

class Asteroid():
    def __init__(self, pos=(0, 0)):
        self.image = pygame.image.load("graphics\Asteroid.png")
        self.pos = pygame.Vector2(pos)

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def click(self):
        mouse = pygame.mouse.get_pos()
        if self.pos == mouse:
            print("Click")

def main():
    pygame.init()
    pygame.display.set_caption("Asteroid Clicker")
    icon = pygame.image.load("graphics\Icon.png")
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((s_width, s_hight))
    bg_tile = pygame.image.load("graphics\starBackground.png").convert()
    asteroid = Asteroid(pos=((s_width//2) - 80, (s_hight//2) - 80))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if pygame.mouse.get_just_pressed()[0]:
            Asteroid.click(asteroid)

        for x in range(0, s_width, bg_tile.get_width()):
            for y in range(0, s_hight, bg_tile.get_height()):
                screen.blit(bg_tile, (x, y))
        
        asteroid.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()