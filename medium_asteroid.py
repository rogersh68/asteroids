from asteroid import Asteroid
from constants import MEDIUM_ROCK_RADIUS, MEDIUM_ROCK_SPIN, MEDIUM_ROCK_SPEED

class MediumAsteroid(Asteroid):
    """
    Defines the medium asteroids
    """
    def __init__(self):
        super().__init__()
        self.img = "images/meteorGrey_med1.png"
        self.radius = MEDIUM_ROCK_RADIUS
        self.spin = MEDIUM_ROCK_SPIN
        self.speed = MEDIUM_ROCK_SPEED
        
    def hit(self):
        # return points
        return 10