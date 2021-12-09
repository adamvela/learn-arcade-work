import random

import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_BEER = 0.035

# --- Increased player speed, as we'll move one 'step'
PLAYER_MOVEMENT_SPEED = 64
beer_collect_sound = arcade.load_sound("arcade_resources_sounds_coin3.wav")
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Snake Game")
        # Variables that will hold sprite lists
        self.player_list = None
        self.beer_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # --- New variables. Timer for tracking each 'step'
        # and speed we'll not put in player sprite, because we'll
        # have a list of them. So put that here
        self.time = 0
        self.change_x = 0
        self.change_y = 0
        self.snake_length = 1

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
        # --- Change this to not be self.player_sprite.change_x but just owned by the class
        if key == arcade.key.UP:
            self.change_y = PLAYER_MOVEMENT_SPEED
            self.change_x = 0

        elif key == arcade.key.DOWN:
            self.change_y = -PLAYER_MOVEMENT_SPEED
            self.change_x = 0

        elif key == arcade.key.LEFT:
            self.change_x = -PLAYER_MOVEMENT_SPEED
            self.change_y = 0

        elif key == arcade.key.RIGHT:
            self.change_x = PLAYER_MOVEMENT_SPEED
            self.change_y = 0

    def update(self, delta_time):

        """ Movement and game logic """
        # --- Keep a timer
        self.time += delta_time
        self.beer_list.update()
        # --- If a certain time has gone by, move

        if self.time > 0.15:
            # --- Reset timer
            self.time = 0

            # --- Create a new character as new head of snake
            player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
            player_sprite.position = self.player_list[-1].position
            player_sprite.center_x += self.change_x
            player_sprite.center_y += self.change_y
            self.player_list.append(player_sprite)

            # --- Remove tail of snake
            while len(self.player_list) > self.snake_length:
                self.player_list[0].remove_from_sprite_lists()

        # Generate a list of all sprites that collided with the player.
        # --- Adjust to check for each segment of the snake
        for player in self.player_list:
            beer_hit_list = arcade.check_for_collision_with_list(player, self.beer_list)

            # Loop through each colliding sprite, remove it, and add to the score.
            for beer in beer_hit_list:
                self.snake_length += 1
                beer.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(beer_collect_sound)

                # Beer image from heineken.com
                beer = arcade.Sprite("heineken-original-bottle.png", SPRITE_SCALING_BEER)

                # Position the beer
                beer.center_x = random.randrange(SCREEN_WIDTH + 20)
                beer.center_y = random.randrange(SCREEN_HEIGHT + 20)

                # Add the beer to the lists
                self.beer_list.append(beer)

        if self.left < 0:
            self.change_x = 0
        if self.right > SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom < 0:
            self.change_y *= -1
        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
