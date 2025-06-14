import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
            self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rando_num = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_vector1 = self.velocity.rotate(rando_num)
            new_vector2 = self.velocity.rotate(-rando_num)
            asteroid1 = Asteroid(new_radius, self.position.x, self.position.y) 
            asteroid2 = Asteroid(new_radius, self.position.x, self.position.y)
            asteroid1.velocity = new_vector1 * 1.2
            asteroid2.velocity = new_vector2 * 1.2
                    


