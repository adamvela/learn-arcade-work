
import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.11
SPRITE_SCALING_BEER = 0.035

# --- Increased player speed, as we'll move one 'step'
PLAYER_MOVEMENT_SPEED = 71

# These two sounds from soundcamp.com
beer_collect_sound = arcade.load_sound("sounds_gulp.wav")
boo_sound = arcade.load_sound("boo.wav")

# Sound comes from https://www.shockwave-sound.com/sound-effects/scream-sounds/Ouche.wav
pain_sound = arcade.load_sound("ouch.wav")

wall_hit_sound = arcade.load_sound("arcade_resources_sounds_error1.wav")
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800


class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """
    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color((235, 192, 52))

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Welcome to the Craven Snake Game", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=35, anchor_x="center")
        arcade.draw_text("Click the mouse to continue", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.4,
                         arcade.color.WHITE, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)


class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions Screen", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 70,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("As we know, Dr.Craven loves his beer.", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 170,
                         arcade.color.BLACK, font_size=48, anchor_x="center")
        arcade.draw_text("Collect the beer to help him with his addiction.", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT - 270, arcade.color.BLACK, font_size=46, anchor_x="center")
        arcade.draw_text("Pressing \"S\" will make the speed of the snake slow.", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 1.8, arcade.color.BLACK, font_size=44, anchor_x="center")
        arcade.draw_text("Pressing \"M\" will make the speed of the snake moderate.", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2.3, arcade.color.BLACK, font_size=43, anchor_x="center")
        arcade.draw_text("Pressing \"F\" will make the speed of the snake fast.", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 3.1, arcade.color.BLACK, font_size=44, anchor_x="center")
        arcade.draw_text("Pressing \"Q\" will quit the game.", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 4.7, arcade.color.BLACK, font_size=44, anchor_x="center")
        arcade.draw_text("Click to the mouse continue.", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 8.8, arcade.color.BLACK, font_size=42, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)


class MyGame(arcade.View):
    """ Our custom Window Class"""
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()
        # Variables that will hold sprite lists
        self.player_list = None
        self.beer_list = None
        self.game_over = False

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
        self.player_speed = 0.15

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.beer_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Face image from
        # https://blog.jetbrains.com/pycharm/2017/07/interview-paul-craven-on-python-gaming-and-teaching/
        self.player_sprite = arcade.Sprite("craven9.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Beer image comes from heineken.com
        beer = arcade.Sprite("heineken-original-bottle.png", SPRITE_SCALING_BEER)

        # Position the beer
        beer.center_x = random.randrange(40, 1480)
        beer.center_y = random.randrange(50, 750)

        # Add the beer to the lists
        self.beer_list.append(beer)

    def on_show(self):
        arcade.set_background_color(arcade.color.BABY_BLUE)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.beer_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        # --- Change this to not be self.player_sprite.change_x but just owned by the class
        if key == arcade.key.S:
            self.player_speed = 0.25

        if key == arcade.key.M:
            self.player_speed = 0.15

        if key == arcade.key.F:
            self.player_speed = 0.05

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

        elif key == arcade.key.Q:
            quit_game_view = QuitGame()
            self.window.show_view(quit_game_view)
            arcade.play_sound(boo_sound)

    def update(self, delta_time):
        """ Movement and game logic """
        # --- Keep a timer
        self.time += delta_time
        self.beer_list.update()
        # --- If a certain time has gone by, move

        if self.time > self.player_speed:
            # --- Reset timer
            self.time = 0

            # --- Create a new character as new head of snake
            player_sprite = arcade.Sprite("craven9.png", SPRITE_SCALING_PLAYER)
            player_sprite.position = self.player_list[-1].position
            player_sprite.center_x += self.change_x
            player_sprite.center_y += self.change_y
            if player_sprite.center_y < 0:
                self.change_y = 0
                self.game_over = True
                game_over_view = GameOverView()
                self.window.show_view(game_over_view)
                arcade.play_sound(wall_hit_sound)

            if player_sprite.center_y > SCREEN_HEIGHT:
                self.change_y = 0
                self.game_over = True
                arcade.play_sound(wall_hit_sound)
                game_over_view = GameOverView()
                self.window.show_view(game_over_view)

            if player_sprite.center_x < 0 or player_sprite.center_x > SCREEN_WIDTH:
                self.change_x = 0
                self.game_over = True
                arcade.play_sound(wall_hit_sound)
                game_over_view = GameOverView()
                self.window.show_view(game_over_view)

            for player in self.player_list:
                snake_hit_list = arcade.check_for_collision_with_list(player, self.player_list)
                if snake_hit_list:
                    self.change_x = 0
                    self.change_y = 0
                    self.game_over = True
                    arcade.play_sound(pain_sound)
                    game_over_view = GameOverView()
                    self.window.show_view(game_over_view)

            if self.game_over:
                return
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
                beer.center_x = random.randrange(40, 1480)
                beer.center_y = random.randrange(50, 750)

                # Add the beer to the lists
                self.beer_list.append(beer)


class QuitGame(arcade.View):
    """ Class to manage the game over view """
    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color((245, 90, 66))

    def on_draw(self):
        """ Draw the game over view """
        arcade.start_render()
        arcade.draw_text("You quit the game.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, 30, anchor_x="center")
        arcade.draw_text("Press the letter \"P\" to play again", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.4,
                         arcade.color.WHITE, 25, anchor_x="center")
        self.window.set_mouse_visible(True)

    def on_key_press(self, key, _modifiers):
        """ If user hits escape, go back to the main menu view """
        if key == arcade.key.P:
            menu_view = MenuView()
            self.window.show_view(menu_view)


class GameOverView(arcade.View):
    """ Class to manage the game over view """
    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color((245, 90, 66))

    def on_draw(self):
        """ Draw the game over view """
        arcade.start_render()
        arcade.draw_text("Game Over you died.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, 30, anchor_x="center")
        arcade.draw_text("Press the letter \"P\" to play again", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.4,
                         arcade.color.WHITE, 25, anchor_x="center")
        self.window.set_mouse_visible(True)

    def on_key_press(self, key, _modifiers):
        """ If user hits escape, go back to the main menu view """
        if key == arcade.key.P:
            menu_view = MenuView()
            self.window.show_view(menu_view)


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Craven Snake Game")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
