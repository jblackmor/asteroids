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
    pygame.display.set_caption('Asteroids')

    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()  # everything that can be updated (inc screen)
    drawable = pygame.sprite.Group()  # everything that can be drawn (inc player, asteroids, shots)
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)  # add all Player instances to these groups
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)  # add all Asteroid instances to these groups
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        updatable.update(dt)

        for a in asteroids:
            if a.check_for_collisions(player):
                print('Game over!')
                sys.exit()
            for s in shots:
                if s.check_for_collisions(a):
                    s.kill()
                    a.split()

        screen.fill(color='black')
        
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()

        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()