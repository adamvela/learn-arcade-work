
import random
import arcade
import math

SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_BALL = 0.06
BALL_COUNT = 20
SPRITE_SCALING_ROCK = 0.06
ROCK_COUNT = 12
ball_collect_sound = arcade.load_sound("../Lab 12 - Final Lab/arcade_resources_sounds_coin3.wav")
rock_collect_sound = arcade.load_sound("arcade_resources_sounds_hurt1.wav")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Rock(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.circle_angle = 0
        self.circle_radius = 0
        self.circle_speed = 0.04
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
                        + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
                        + self.circle_center_y
        self.circle_angle += self.circle_speed


class Ball(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1
        if self.right > SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom < 0:
            self.change_y *= -1
        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")
        # Variables that will hold sprite lists
        self.player_list = None
        self.ball_list = None
        self.rock_list = None
        self.coordinates = []

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Hid the cursor
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from annimaker.com
        self.player_sprite = arcade.Sprite("sports-tennis.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the ball
        for i in range(BALL_COUNT):
            # Create the ball instance
            # Image from clipart-library.com
            ball = Ball("ball.png", SPRITE_SCALING_BALL)

            # Position the ball
            ball.center_x = random.randrange(SCREEN_WIDTH)
            ball.center_y = random.randrange(SCREEN_HEIGHT)
            ball.change_x = random.randrange(-3, 4)
            ball.change_y = random.randrange(-3, 4)
            # Add the ball to the lists
            self.ball_list.append(ball)

        for i in range(ROCK_COUNT):
            # Create the ball instance
            # Rock image from pinclipart.com
            rock = Rock("rock.png", SPRITE_SCALING_ROCK)

            # Position the rock
            rock.circle_center_x = random.randrange(SCREEN_WIDTH)
            rock.circle_center_y = random.randrange(SCREEN_HEIGHT)
            rock.circle_radius = random.randrange(10, 200)
            rock.circle_angle = random.random() * 2 * math.pi
            # Add the rock to the lists
            self.rock_list.append(rock)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.ball_list.draw()
        self.player_list.draw()
        self.rock_list.draw()

        # Put text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        if len(self.ball_list) == 0:
            game = "GAME OVER"
            arcade.draw_text(game, 325, 300, arcade.color.WHITE, 20)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        if len(self.ball_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y
        elif len(self.ball_list) == 0:
            self.set_mouse_visible(True)

    def update(self, delta_time):
        """ Movement and game logic """
        if len(self.ball_list) > 0:
            self.ball_list.update()
            self.rock_list.update()
            # Generate a list of all sprites that collided with the player.
            good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.ball_list)
            bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.rock_list)

            # Loop through each colliding sprite, remove it, and add to the score or subtract from the score.
            for ball in good_hit_list:
                ball.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(ball_collect_sound)

            for rock in bad_hit_list:
                rock.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound(rock_collect_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
