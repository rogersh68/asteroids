import random
import math
from flyingobject import FlyingObject

class Asteroid(FlyingObject):
    """
    Base class for asteroids. Asteroids are random, have spin, and
    change when they are hit.
    """
    def __init__(self):
        super().__init__()
        self.direction = random.randint(1, 50)
        self.spin = 0.0
        self.speed = 0.0
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        
    def advance(self):
        # Copy base advance method
        super().advance()
        
        # Add spin
        self.angle += self.spin
        
    def hit(self):
        # Each ateroid will return points depending on size
        return 0