from asteroid import Asteroid
from constants import SMALL_ROCK_RADIUS, SMALL_ROCK_SPIN

class SmallAsteroid(Asteroid):
    """
    Defines the smallest asteroids
    """
    def __init__(self):
        super().__init__()
        self.img = "images/meteorGrey_small1.png"
        self.radius = SMALL_ROCK_RADIUS
        self.spin = SMALL_ROCK_SPIN
        
    def hit(self):
        # Kill the asteroid
        self.alive = False
        # Return points
        return 15