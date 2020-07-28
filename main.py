import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 900,700
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invader")

#Enemy Ships
RED_SPACE_SHIP = pygame.image.load(os.path.join("pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("pixel_ship_blue_small.png"))

#Players ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("pixel_ship_yellow.png"))

#Lasers and background
BLUE_LASER = pygame.image.load(os.path.join("pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(os.path.join("pixel_laser_green.png"))
RED_LASER = pygame.image.load(os.path.join("pixel_laser_red.png"))
YELLOW_LASER = pygame.image.load(os.path.join("pixel_laser_yellow.png"))

BG = pygame.transform.scale(pygame.image.load(os.path.join("background-black.png")), (WIDTH, HEIGHT))

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self,window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50))


def main():
    run = True
    FPS = 60
    level = 1
    lives = 3
    player_vel = 5
    main_font = pygame.font.SysFont("comicsans",40)
    clock = pygame.time.Clock()

    ship = Ship(425, 640)

    def redraw_window():
        WIN.blit(BG, (0,0))
        #draw text
        level_label = main_font.render(f"Level: {level}",1,(255,255,255))
        lives_label = main_font.render(f"Lives: {lives}",1,(255,255,255))

        WIN.blit(lives_label, (WIDTH - level_label.get_width() - 30,10))
        WIN.blit(level_label, (30,10))

        ship.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ship.x - player_vel > 0: #left
            ship.x -= player_vel
        if keys[pygame.K_RIGHT] and ship.x + player_vel + 50 < WIDTH: #right
            ship.x += player_vel
        if keys[pygame.K_UP] and ship.y - player_vel > 0: #up
            ship.y -= player_vel
        if keys[pygame.K_DOWN] and ship.y + player_vel + 50 < HEIGHT: #down
            ship.y += player_vel

main()