import math
from flyingobject import FlyingObject
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SHIP_RADIUS, SHIP_THRUST_AMOUNT, SHIP_TURN_AMOUNT

class Ship(FlyingObject):
    """
    Defines a Ship object. Adds movements to methods.
    """
    def __init__(self):
        super().__init__()
        self.img = "images/playerShip1_orange.png"
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.radius = SHIP_RADIUS
        self.speed = SHIP_THRUST_AMOUNT
        self.angle = 1
        self.lives = 3
        
    def turn_left(self):
        self.angle += SHIP_TURN_AMOUNT
        
    def turn_right(self):
        self.angle -= SHIP_TURN_AMOUNT
        
    def move_forward(self):
        self.velocity.dx -= math.sin(math.radians(self.angle)) * self.speed
        self.velocity.dy += math.cos(math.radians(self.angle)) * self.speed
        
    def move_backward(self):
        self.velocity.dx += math.sin(math.radians(self.angle)) * self.speed
        self.velocity.dy -= math.cos(math.radians(self.angle)) * self.speed
        
    def hit(self):
        # If ship is out of lives change image to explosion, kill it, and don't let it move
        if self.lives <= 0:
            self.img = "images/blast.png"
            self.alive = False
            self.speed = 0
            self.velocity.dx = 0
            self.velocity.dy = 0
        # Remove a life for each hit    
        else:
            self.lives -= 1