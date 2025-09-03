# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

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
            
        # rotate player object
        updatable.update(dt)

        # to check collision between player and asteroids
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit()

            # to check collision between shots and asteroids
            for shot in shots:
                if shot.collides(asteroid):
                    shot.kill()
                    asteroid.kill()

        # fill the Surface with a solid color
        screen.fill("black") 

        # draw player (hitbox (triangle(circle))
        for d in drawable:
            d.draw(screen)
            # player.draw(screen) // instead of this, we use the drawable because our Player objects are part of the drawable group

        # update the contents of the entire display
        pygame.display.flip() 

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
