import math
from flyingobject import FlyingObject
from constants import BULLET_RADIUS, BULLET_SPEED, BULLET_LIFE

class Bullet(FlyingObject):
    """
    Defines bullet objects. Adds a fire method and updated
    advance method
    """
    def __init__(self, shipX, shipY, shipAngle):
        super().__init__()
        self.img = "images/laserBlue01.png"
        self.radius = BULLET_RADIUS
        self.speed = BULLET_SPEED
        self.life = BULLET_LIFE
        self.center.x = shipX
        self.center.y = shipY
        self.angle = shipAngle
        
    def fire(self):
        self.velocity.dx -= math.sin(math.radians(self.angle - 270)) * self.speed
        self.velocity.dy += math.cos(math.radians(self.angle - 270)) * self.speed
        
    def advance(self):
        # Copy base advance method
        super().advance()
        
        # Add bullet life span to method
        self.life -= 1
        if (self.life <= 0):
            self.alive = False
            
    def hit(self):
        # Kill bullet when it hits asteroid
        self.alive = False
