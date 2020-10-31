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
        self.spin = 0.0
        self.speed = 0.0
        
    def advance(self):
        # Copy base advance method
        super().advance()
        
        # Add spin
        self.angle += self.spin
        
    def hit(self):
        # Each ateroid will return points depending on size
        return 0