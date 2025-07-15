# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 # delta time

    print(f"""
    Starting Asteroids!
    Screen width: {SCREEN_WIDTH}
    Screen height: {SCREEN_HEIGHT}
        """)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # creates a display Surface

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fill the Surface with a solid color
        screen.fill("black") 
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
        player.draw(screen)
        # update the contents of the entire display
        pygame.display.flip() 

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
