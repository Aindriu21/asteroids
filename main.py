import sys
import pygame
from constants import *
from player import Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = ( updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for thing in updatable:
            thing.update(dt) 

        screen.fill("black")
        
        for thing in drawable:
            thing.draw(screen)


        pygame.display.flip()

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collides(asteroid):
                    #pygame.sprite.Sprite.kill(asteroid)
                    #pygame.sprite.Sprite.kill(bullet)
                    bullet.kill()
                    asteroid.split()
                    

            if asteroid.collides(player):
                print("Game over!")
                sys.exit()

            
        
        # limiting the framework to 60 FPS
        dt = clock.tick(60)
        dt /= 1000


if __name__ == "__main__":
	main()
