from turtle import position

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self,dt):
        self.position += self.velocity*dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle=random.uniform(20,50)
        v1=self.velocity.rotate(angle)
        v2=self.velocity.rotate(-angle)
        new_asteroid1=Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)
        new_asteroid2=Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)
        new_asteroid1.velocity=v1*1.2
        new_asteroid2.velocity=v2
