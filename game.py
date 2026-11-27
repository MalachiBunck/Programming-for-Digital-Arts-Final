import sys

import pygame

s_width = 640
s_hight = 480
clicks = 0
drills = 0

content_height = 800
scroll_y = 0

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

class Drill():
    def __init__(self, pos=(0, 0)):
        self.image = pygame.image.load("graphics\drill.png")
        self.pos = pygame.Vector2(pos)

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def click(self, mouse_pos, button_rad):
        global clicks
        global drills
        mouse_x, mouse_y = mouse_pos
        self_x, self_y = self.pos
        button_dist = pygame.math.Vector2(mouse_x - (self_x + 80), mouse_y - (self_y + 40)).length()
        if button_dist <= button_rad:
            if clicks >= 20:
                clicks -= 20
                drills += 1
            else:
                print("no")

def main():
    pygame.init()
    pygame.display.set_caption("Asteroid Clicker")
    icon = pygame.image.load("graphics\Icon.png")
    pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((s_width, s_hight))
    content = pygame.Surface((s_width, content_height))

    bg_tile = pygame.image.load("graphics\starBackground.png").convert()
    bg_shop = pygame.image.load("graphics\shop_bg.png")
    asteroid = Asteroid(pos=((s_width//2) - 80, (s_hight//2) - 80))
    drill = Drill(pos=((s_width//4) - 80, (content_height - 200) - 80))

    last_click_time = pygame.time.get_ticks()
    running = True

    font = pygame.font.SysFont("Arial", 25, True)
    font_small = pygame.font.SysFont("Arial", 20, True)
    text_display = font.render("Click the asteroid to mine", True, (255, 255, 255), None, 200)
    shop_text = font_small.render("Cost: 20 asteroids", True, (255, 255, 255), None, 200)
    

    global scroll_y
    global clicks
    global drills

    while running:

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            if event.type == pygame.MOUSEWHEEL:
                scroll_y -= event.y * 30
            drill_text = font_small.render("Auto mining: " + str(drills) + "\s", True, (255, 255, 255), None, 200)

        scroll_y = max(0, min(scroll_y, content_height - s_hight))

        current_time = pygame.time.get_ticks()

        if drills >= 1:
            if current_time - last_click_time >= 1000:
                clicks += drills
                last_click_time = current_time
                
                

        if pygame.mouse.get_just_pressed()[0]:
            adjusted_mouse = (mouse_pos[0], mouse_pos[1] + scroll_y)
            asteroid.click(adjusted_mouse, button_rad=100)
            drill.click(adjusted_mouse, button_rad=100)
            

        for x in range(0, s_width, bg_tile.get_width()):
            for y in range(0, content_height, bg_tile.get_height()):
                content.blit(bg_tile, (x, y))

        text_display = font.render("Asteroids mined: " + str(clicks), True, (255, 255, 255), None, 200)

        content.blit(bg_shop, (0, 440))
        content.blit(text_display, (225, 120))
        content.blit(drill_text, (255, 330))
        content.blit(shop_text, (80, 600))
        asteroid.draw(content)
        drill.draw(content)
        screen.blit(content, (0, 0), (0, scroll_y, s_width, s_hight))
        pygame.display.flip()

if __name__ == "__main__":
    main()