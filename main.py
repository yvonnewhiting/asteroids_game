import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while pygame.init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            updateable.update(dt)

            screen.fill("black")

            for item in drawable:
                item.draw(screen)
        
            pygame.display.flip()

            dt = clock.tick(60) / 1000
    
    

if __name__ == "__main__":
    main()