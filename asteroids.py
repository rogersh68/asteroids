"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
File updated and completed by: Hannah Rogers
"""

#imports
import arcade

from ship import Ship
from bullet import Bullet
from big_asteroid import BigAsteroid
from medium_asteroid import MediumAsteroid
from small_asteroid import SmallAsteroid

#constants
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, INITIAL_ROCK_COUNT, WINNING_SCORE


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # Track each game object
        self.asteroids = []
        
        # Start with 5 asteroids
        for asteroid in range (0, INITIAL_ROCK_COUNT):
            self.asteroids.append(BigAsteroid())

        self.ship = Ship()
        
        self.bullets = []
        
        # Start game with 0 points
        self.score = 0

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # Draw each object
        for asteroid in self.asteroids:
            asteroid.draw()
        
        self.ship.draw()
        
        for bullet in self.bullets:
            bullet.draw()
            
        # Draw the lives(hearts)
        self.draw_lives()
            
        # Draw the score
        self.draw_score()
           
        # Write game over if ship is dead   
        if self.ship.alive == False:
            self.game_over()
            
        # Write you won if score is 200+
        if self.score >= WINNING_SCORE:
            self.game_win()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # Tell everything to advance or move forward one step in time
        for asteroid in self.asteroids:
            asteroid.advance()
        
        self.ship.advance()
        
        for bullet in self.bullets:
            bullet.advance()
   
        # Check for collisions
        self.check_collisions()

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        """
        if arcade.key.LEFT in self.held_keys:
            # turn the ship to the left
            self.ship.turn_left()

        if arcade.key.RIGHT in self.held_keys:
            # turn the ship to the right
            self.ship.turn_right()

        if arcade.key.UP in self.held_keys:
            # move the ship forward
            self.ship.move_forward()

        if arcade.key.DOWN in self.held_keys:
            # move the ship backward
            self.ship.move_backward()


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            # fire bullets with space bar
            if key == arcade.key.SPACE:
                bullet = Bullet(self.ship.center.x, self.ship.center.y, self.ship.angle)
                self.bullets.append(bullet)
                bullet.fire()

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)
            
    def remove_dead_objects(self):
        """
        Removes objects that are no longer alive
        """
        for asteroid in self.asteroids:
            if (asteroid.alive == False):
                self.asteroids.remove(asteroid)
                
        for bullet in self.bullets:
            if (bullet.alive == False):
                self.bullets.remove(bullet)
                
    def check_collisions(self):
        """
        Checks for collisons between objects
        """
        # Check if bullets hit rocks
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                # Check if objects are alive
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius
                    if (abs(bullet.center.x - asteroid.center.x) < too_close and
                        abs(bullet.center.y - asteroid.center.y) < too_close):
                        # Kill the bullet
                        bullet.hit()
                        # Get points for hitting asteroid with bullet
                        self.score += asteroid.hit()
                        # Break the asteroid apart
                        self.break_asteroid(asteroid)
            
            
        # Check if rocks hit ship
        for asteroid in self.asteroids:
            # Check if objects are alive
            if asteroid.alive and self.ship.alive:
                too_close = asteroid.radius + self.ship.radius
                if (abs(asteroid.center.x - self.ship.center.x) < too_close and
                    abs(asteroid.center.y - self.ship.center.y) < too_close):
                    # Remove ship life
                    self.ship.hit()
                    # Kill the asteroid
                    asteroid.alive = False
            
        # Remove dead objects
        self.remove_dead_objects()
        
    def break_asteroid(self, asteroid):
        """
        Checks the type of asteroid that was hit and
        breaks the asteroid apart based on the rules.
        """
        # Check if asteroid object is Big
        if type(asteroid) is BigAsteroid:
            # Remove old asteroid
            old = self.asteroids.pop(self.asteroids.index(asteroid))
            
            # Create first medium asteroid
            med1 = MediumAsteroid()
            med1.center.x = old.center.x
            med1.center.y = old.center.y
            med1.velocity.dy = old.velocity.dy + 2
            med1.velocity.dx = old.velocity.dx + 1
            
            # Create second medium asteroid
            med2 = MediumAsteroid()
            med2.center.x = old.center.x
            med2.center.y = old.center.y
            med2.velocity.dy = old.velocity.dy - 2
            
            # Create small asteroid
            small = SmallAsteroid()
            small.center.x = old.center.x
            small.center.y = old.center.y
            small.velocity.dx = old.velocity.dx + 5
            
            # add new asteroids to the asteroids array
            self.asteroids.extend([med1, med2, small])
          
        # Check if asteroid object is Medium
        elif type(asteroid) is MediumAsteroid:
            # Remove old asteroid
            old = self.asteroids.pop(self.asteroids.index(asteroid))
            
            # Create first small asteroid
            small1 = SmallAsteroid()
            small1.center.x = old.center.x
            small1.center.y = old.center.y
            small1.velocity.dx = old.velocity.dx + 1.5
            small1.velocity.dy = old.velocity.dy + 1.5
            
            # Create second small asteroid
            small2 = SmallAsteroid()
            small2.center.x = old.center.x
            small2.center.y = old.center.y
            small2.velocity.dx = old.velocity.dx - 1.5
            small2.velocity.dy = old.velocity.dy - 1.5
            
            # add new asteroids to the asteroids array
            self.asteroids.extend([small1, small2])
            
    def game_over(self):
        """
        When ship is dead write "Game Over" on the center
        of the screen
        """
        # Get center of the screen
        start_y = SCREEN_HEIGHT / 2
        start_x = SCREEN_WIDTH / 2
        
        # Draw text
        arcade.draw_text("GAME OVER",
                         start_x, start_y,
                         arcade.color.WHITE,
                         40,
                         width=400,
                         align="center",
                         anchor_x="center",
                         anchor_y="center")
        
    def game_win(self):
        """
        When player scores 200 points write "You Win"
        on the center of the screen and kill all asteroids
        """
        # Kill all asteroids
        for asteroid in self.asteroids:
            asteroid.alive = False
                        
        # Get center of the screen
        start_y = SCREEN_HEIGHT / 2
        start_x = SCREEN_WIDTH / 2
        
        # Draw text
        arcade.draw_text("YOU WON!",
                         start_x, start_y,
                         arcade.color.WHITE,
                         40,
                         width=400,
                         align="center",
                         anchor_x="center",
                         anchor_y="center")
        
    def draw_score(self):
        """
        Draws the score on the screen
        """
        # format score text
        score_text = "Score: {}".format(self.score)
        
        # Get bottom left of screen
        start_x = 20
        start_y = 60
        
        # Draw text
        arcade.draw_text(score_text,
                         start_x,
                         start_y,
                         font_size=20,
                         color=arcade.color.WHITE)
        
    def draw_lives(self):
        """
        Draws the number of lives of the ship,
        represented with hearts.
        """
        # Get bottom left of screen
        start_x = 30
        start_y = 30
        
        # Draw the number of lives
        for life in range(0, self.ship.lives):
            texture = arcade.load_texture("images/life.png")
            arcade.draw_texture_rectangle(start_x, start_y, texture.width, texture.height, texture, 0, 255)
            # Move each heart over by 40
            start_x += 40


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()