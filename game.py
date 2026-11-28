import sys

import pygame

s_width = 640
s_hight = 480

score = 0
drills = 0
click_amount = 1
drill_upgrade = 1
du_cost = 100
drill_cost = 20
click_cost = 30

content_height = 800
scroll_y = 0

class Asteroid():
    def __init__(self, pos=(0, 0)):
        self.image = pygame.image.load("graphics\Asteroid.png")
        self.pos = pygame.Vector2(pos)

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def click(self, mouse_pos, button_rad):
        global click_amount
        global score
        mouse_x, mouse_y = mouse_pos
        self_x, self_y = self.pos
        button_dist = pygame.math.Vector2(mouse_x - (self_x + 80), mouse_y - (self_y + 80)).length()
        if button_dist <= button_rad:
            score += click_amount

class Drill():
    def __init__(self, pos=(0, 0)):
        self.image = pygame.image.load("graphics\drill.png")
        self.pos = pygame.Vector2(pos)

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def click(self, mouse_pos, button_rad):
        global score
        global drills
        global drill_cost
        mouse_x, mouse_y = mouse_pos
        self_x, self_y = self.pos
        button_dist = pygame.math.Vector2(mouse_x - (self_x + 80), mouse_y - (self_y + 40)).length()
        if button_dist <= button_rad:
            if score >= drill_cost:
                score -= drill_cost
                drill_cost *= 2
                drills += 1
            else:
                return

class Click_Upgrade():
    def __init__(self, pos=(0, 0)):

            self.image = pygame.image.load("graphics/upgrade.png")
            self.pos = pygame.Vector2(pos)
    
    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def click(self, mouse_pos, button_rad):
        global score
        global click_amount
        global click_cost
        mouse_x, mouse_y = mouse_pos
        self_x, self_y = self.pos
        button_dist = pygame.math.Vector2(mouse_x - (self_x + 80), mouse_y - (self_y + 40)).length()
        if button_dist <= button_rad:
            if score >= click_cost:
                score -= click_cost
                click_cost += 30
                click_amount += 1
            else:
                return

class Drill_Upgrade():
    def __init__(self, pos=(0, 0)):
            self.image = pygame.image.load("graphics/d_upgrade.png")
            self.pos = pygame.Vector2(pos)
    
    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def click(self, mouse_pos, button_rad):
        global score
        global drill_upgrade
        global du_cost
        mouse_x, mouse_y = mouse_pos
        self_x, self_y = self.pos
        button_dist = pygame.math.Vector2(mouse_x - (self_x + 80), mouse_y - (self_y + 40)).length()
        if button_dist <= button_rad:
            if score >= du_cost:
                score -= du_cost
                drill_upgrade += 1
                du_cost *= 2
            else:
                return

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
    upgrade = Click_Upgrade(pos=((s_width - 160) - 80, (content_height - 200) - 80))
    d_upgrade = Drill_Upgrade(pos=((s_width//4) - 80, (content_height - 50) - 80))

    last_click_time = pygame.time.get_ticks()
    running = True

    save_data = {}
    try:
        with open("save.txt", "r") as file:
            for line in file:
                if ":" in line:
                    key, value = line.strip().split(":", 1)
                    save_data[key.strip()] = int(value.strip())
    except FileNotFoundError:
        pass

    font = pygame.font.SysFont("Arial", 25, True)
    font_small = pygame.font.SysFont("Arial", 20, True)
    text_display = font.render("Click the asteroid to mine", True, (255, 255, 255), None, 200)
    drill_text_cost = font_small.render("Cost: 20 asteroids", True, (255, 255, 255), None)
    drill_title = font_small.render("Auto Miner", True, (255, 255, 255), None)
    upgrade_title = font_small.render("Drill Size", True, (255, 255, 255), None)
    upgrade_cost = font_small.render("Cost: 30 asteroids", True, (255, 255, 255), None)
    du_text_cost = font_small.render("Cost: 100 asteroids", True, (255, 255, 255), None)
    du_text_title = font_small.render("Auto Miner Upgrade", True, (255, 255, 255), None)

    global scroll_y
    global score
    global drills
    global click_amount
    global drill_upgrade
    global du_cost
    global click_cost
    global drill_cost

    if "score" in save_data:
        score = save_data["score"]
    else:
        score = 0
        
    if "drills" in save_data:
        drills = save_data["drills"]
    else:
        drills = 0

    if "click_amount" in save_data:
        click_amount = save_data["click_amount"]
    else:
        click_amount = 1

    if "drill_upgrade" in save_data:
        drill_upgrade = save_data["drill_upgrade"]
    else:
        drill_upgrade = 1

    if "du_cost" in save_data:
        du_cost = save_data["du_cost"]
    else:
        du_cost = 100

    if "click_cost" in save_data:
        click_cost = save_data["click_cost"]
    else:
        click_cost = 30

    if "drill_cost" in save_data:
        drill_cost = save_data["drill_cost"]
    else:
        drill_cost = 20

    while running:

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("save.txt", "w") as file:
                    file.write(f"score: {score}\n")
                    file.write(f"drills: {drills}\n")
                    file.write(f"click_amount: {click_amount}\n")
                    file.write(f"drill_upgrade: {drill_upgrade}\n")
                    file.write(f"du_cost: {du_cost}\n")
                    file.write(f"click_cost: {click_cost}\n")
                    file.write(f"drill_cost: {drill_cost}\n")
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                with open("save.txt", "w") as file:
                    file.write(f"score: {score}\n")
                    file.write(f"drills: {drills}\n")
                    file.write(f"click_amount: {click_amount}\n")
                    file.write(f"drill_upgrade: {drill_upgrade}\n")
                    file.write(f"du_cost: {du_cost}\n")
                running = False
            if event.type == pygame.MOUSEWHEEL:
                scroll_y -= event.y * 30

            drill_text = font_small.render("Auto mining: " + str(drills * drill_upgrade) + "\s", True, (255, 255, 255), None, 200)
            upgrade_text = font_small.render("Asteroids per Click: " + str(click_amount), True, (255, 255, 255), None, 200)
            du_text_cost = font_small.render("Cost: " + str(du_cost) + " asteroids", True, (255, 255, 255), None)
            upgrade_cost = font_small.render("Cost: "+ str(click_cost) +" asteroids", True, (255, 255, 255), None)
            drill_text_cost = font_small.render("Cost: "+ str(drill_cost) +" asteroids", True, (255, 255, 255), None)

        scroll_y = max(0, min(scroll_y, content_height - s_hight))

        current_time = pygame.time.get_ticks()

        if drills >= 1:
            if current_time - last_click_time >= 1000:
                score += drills * drill_upgrade
                last_click_time = current_time
                
                

        if pygame.mouse.get_just_pressed()[0]:
            adjusted_mouse = (mouse_pos[0], mouse_pos[1] + scroll_y)
            asteroid.click(adjusted_mouse, button_rad=100)
            drill.click(adjusted_mouse, button_rad=100)
            upgrade.click(adjusted_mouse, button_rad=100)
            d_upgrade.click(adjusted_mouse, button_rad=100)
            

        for x in range(0, s_width, bg_tile.get_width()):
            for y in range(0, content_height, bg_tile.get_height()):
                content.blit(bg_tile, (x, y))

        text_display = font.render("Asteroids mined: " + str(score), True, (255, 255, 255), None, 200)

        content.blit(bg_shop, (0, 440))
        content.blit(text_display, (225, 120))
        content.blit(drill_text, (255, 330))
        content.blit(drill_text_cost, (80, 600))
        content.blit(drill_title, (100, 500))
        content.blit(upgrade_text, (237, 355))
        content.blit(upgrade_cost, (420, 600))
        content.blit(upgrade_title, (450, 500))
        content.blit(du_text_cost, (80, 750))
        content.blit(du_text_title, (80, 650))
        asteroid.draw(content)
        drill.draw(content)
        upgrade.draw(content)
        d_upgrade.draw(content)
        screen.blit(content, (0, 0), (0, scroll_y, s_width, s_hight))
        pygame.display.flip()

if __name__ == "__main__":
    main()