import sys

import pygame

s_width = 640
s_hight = 480
clicks = 0

class Asteroid():
    def __init__(self, pos=(0, 0)):
        self.image = pygame.image.load("graphics\Asteroid.png")
        self.pos = pygame.Vector2(pos)

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def click(self, mouse_pos, button_rad):
        mouse_x, mouse_y = mouse_pos
        self_x, self_y = self.pos
        button_dist = pygame.math.Vector2(mouse_x - (self_x + 80), mouse_y - (self_y + 80)).length()
        if button_dist <= button_rad:
            global clicks
            clicks += 1

def main():
    pygame.init()
    pygame.display.set_caption("Asteroid Clicker")
    icon = pygame.image.load("graphics\Icon.png")
    pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((s_width, s_hight))
    bg_tile = pygame.image.load("graphics\starBackground.png").convert()
    asteroid = Asteroid(pos=((s_width//2) - 80, (s_hight//2) - 80))
    
    running = True

    font = pygame.font.SysFont("Arial", 20)
    text_display = font.render("Click the asteroid to mine", True, (255, 255, 255))

    while running:

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False


        if pygame.mouse.get_just_pressed()[0]:
            asteroid.click(mouse_pos, button_rad=100)
            text_display = font.render("Asteroids mined: " + str(clicks), True, (255, 255, 255))

        for x in range(0, s_width, bg_tile.get_width()):
            for y in range(0, s_hight, bg_tile.get_height()):
                screen.blit(bg_tile, (x, y))

        
        screen.blit(text_display, (250, 100))
        asteroid.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()