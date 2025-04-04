import sys    #Exit game
import pygame #Contains the functions needed to develop games
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #Initialize pygame settings and screen objects
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Create a ship
    ship = Ship(ai_settings,screen)
    #Create a group to store bullets
    bullets = Group()
    bg_color = (230, 230, 230)

    #Start the main game loop
    while True:
        #Monitor keyboard and mouse events
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()