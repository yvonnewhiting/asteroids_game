import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while pygame.init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            screen.fill("black")
    
    

if __name__ == "__main__":
    main()