import random
from asteroid import Asteroid
from constants import BIG_ROCK_RADIUS, BIG_ROCK_SPIN, BIG_ROCK_SPEED

class BigAsteroid(Asteroid):
    """
    Defines the biggest asteroids
    """
    def __init__(self):
        super().__init__()
        self.center.x = random.randint(1, 50)
        self.center.y = random.randint(1, 150)
        self.img = "images/meteorGrey_big1.png"
        self.radius = BIG_ROCK_RADIUS
        self.spin = BIG_ROCK_SPIN
        self.speed = BIG_ROCK_SPEED
        
    def hit(self):
        # return points
        return 5