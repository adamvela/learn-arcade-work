""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_BEER = 0.035
PLAYER_MOVEMENT_SPEED = 5

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.beer_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.beer_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Beer image comes from heineken.com
        beer = arcade.Sprite("heineken-original-bottle.png", SPRITE_SCALING_BEER)

        # Position the beer
        beer.center_x = random.randrange(SCREEN_WIDTH)
        beer.center_y = random.randrange(SCREEN_HEIGHT)

        # Add the beer to the lists
        self.beer_list.append(beer)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.beer_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def update(self, delta_time):
        """ Movement and game logic """
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.beer_list.update()
        self.player_list.update()
        # Generate a list of all sprites that collided with the player.
        beer_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.beer_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for beer in beer_hit_list:
            beer.remove_from_sprite_lists()
            self.score += 1
            # Coin image from kenney.nl
            beer = arcade.Sprite("heineken-original-bottle.png", SPRITE_SCALING_BEER)

            # Position the coin
            beer.center_x = random.randrange(SCREEN_WIDTH)
            beer.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.beer_list.append(beer)
            self.player_list.draw()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()