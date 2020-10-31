import arcade
from abc import ABC
from abc import abstractmethod
from point import Point
from velocity import Velocity
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class FlyingObject(ABC):
    """
    Base class that defines general methods and properties
    of objects that fly in the game.
    """
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True
        self.img = ""
        self.radius = 0.0
        self.angle = 0.0
        self.speed = 0.0
        self.direction = 0.0
        self.alpha = 255
        
    def draw(self):
        texture = arcade.load_texture(self.img)

        width = texture.width
        height = texture.height

        arcade.draw_texture_rectangle(self.center.x, self.center.y, width, height, texture, self.angle, self.alpha)
    
    def advance(self):
        # Check for wrap everytime it advances
        self.wrap()
        
        # Advance
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    def wrap(self):
        # Horizontal wrap
        if (self.center.x > SCREEN_WIDTH):
            self.center.x = 0
        if (self.center.x < 0):
            self.center.x = SCREEN_WIDTH
        
        # Vertical wrap
        if (self.center.y > SCREEN_HEIGHT):
            self.center.y = 0
        if (self.center.y < 0):
            self.center.y = SCREEN_HEIGHT
    
    @abstractmethod
    def hit(self):
        """
        each flying object can be hit, but will implement different
        logic based on object type.
        """
        pass