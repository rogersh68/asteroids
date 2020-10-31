import random
import math
from asteroid import Asteroid
from constants import BIG_ROCK_RADIUS, BIG_ROCK_SPIN, BIG_ROCK_SPEED, SCREEN_HEIGHT

class BigAsteroid(Asteroid):
    """
    Defines the biggest asteroids
    """
    def __init__(self):
        super().__init__()
        self.center.x = random.randint(1, 70)
        self.center.y = random.randint(1, SCREEN_HEIGHT)
        self.img = "images/meteorGrey_big1.png"
        self.radius = BIG_ROCK_RADIUS
        self.spin = BIG_ROCK_SPIN
        self.velocity.dx = BIG_ROCK_SPEED
        self.velocity.dy = BIG_ROCK_SPEED
        
    def hit(self):
        # return points
        return 5