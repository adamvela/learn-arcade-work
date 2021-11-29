""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_CRAVEN = 0.5
SPRITE_SCALING_BEER = 0.2
CRAVEN_MOVEMENT_SPEED = 5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.craven_list = None
        self.beer_list = None

        # Set up the player info
        self.craven_sprite = None
        self.score = 0

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.craven_list = arcade.SpriteList()
        self.beer_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.craven_sprite = arcade.Sprite("character.png", SPRITE_SCALING_CRAVEN)
        self.craven_sprite.center_x = 50
        self.craven_sprite.center_y = 50
        self.craven_list.append(self.craven_sprite)

        beer = arcade.Sprite("coin_01.png", SPRITE_SCALING_BEER)

        # Position the coin
        beer.center_x = random.randrange(SCREEN_WIDTH)
        beer.center_y = random.randrange(SCREEN_HEIGHT)

        # Add the coin to the lists
        self.beer_list.append(beer)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.beer_list.draw()
        self.craven_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP:
            self.craven_sprite.change_y = CRAVEN_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.craven_sprite.change_y = -CRAVEN_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.craven_sprite.change_x = -CRAVEN_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.craven_sprite.change_x = CRAVEN_MOVEMENT_SPEED

    def update(self, delta_time):
        """ Movement and game logic """
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.beer_list.update()

        # Generate a list of all sprites that collided with the player.
        beers_hit_list = arcade.check_for_collision_with_list(self.craven_sprite, self.beer_list)
        # Loop through each colliding sprite, remove it, and add to the score.
        for beer in beers_hit_list:
            beer.remove_from_sprite_lists()
            self.score += 1
            if beer in beers_hit_list == 0:
                beer.center_x = random.randrange(SCREEN_WIDTH)
                beer.center_y = random.randrange(SCREEN_HEIGHT)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
