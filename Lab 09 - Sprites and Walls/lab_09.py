"""
Scroll around a large screen.

Artwork from https://api.arcade.academy/en/latest/resources.html

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import arcade

SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
VIEWPORT_MARGIN = 220
SCREEN_TITLE = "Lab 9"
CAMERA_SPEED = 0.1
PLAYER_MOVEMENT_SPEED = 7
eat_sound = arcade.load_sound("arcade_resources_sounds_secret4.wav")


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.score = 0
        self.worm_list = None

        # Set up the player
        self.player_sprite = None

        # Physics engine
        self.physics_engine = None

        # Create the cameras.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("frog_move.png",
                                           scale=0.4)
        self.player_sprite.center_x = 310
        self.player_sprite.center_y = 425
        self.player_list.append(self.player_sprite)

        self.score = 0
        self.worm_list = arcade.SpriteList()

        # Draw Border
        for x in range(173, 1400, 64):
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        for y in range(350, 1125, 64):
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING)
            wall.center_x = 109
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(173, 1400, 64):
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1118
            self.wall_list.append(wall)

        for y in range(350, 1125, 64):
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING)
            wall.center_x = 1390
            wall.center_y = y
            self.wall_list.append(wall)

        # Draw inside maze
        coordinate_list_1 = [[250, 500],
                             [314, 500],
                             [450, 500],
                             [514, 500],
                             [700, 500],
                             [764, 500],
                             [828, 500],
                             [960, 500],
                             [1100, 500],
                             [1164, 500],
                             [1228, 500]]

        for coordinate in coordinate_list_1:
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list_2 = [[173, 625],
                             [237, 625],
                             [450, 625],
                             [514, 625],
                             [578, 625],
                             [642, 625],
                             [828, 625],
                             [892, 625],
                             [956, 625],
                             [1124, 625],
                             [1174, 625],
                             [1326, 625]]

        for coordinate in coordinate_list_2:
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list_3 = [[173, 750],
                             [314, 750],
                             [378, 750],
                             [442, 750],
                             [570, 750],
                             [764, 750],
                             [828, 750],
                             [960, 750],
                             [1024, 750],
                             [1224, 750],
                             [1288, 750]]

        for coordinate in coordinate_list_3:
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list_4 = [[173, 875],
                             [237, 875],
                             [374, 875],
                             [514, 875],
                             [578, 875],
                             [700, 875],
                             [764, 875],
                             [900, 875],
                             [964, 875],
                             [1100, 875],
                             [1164, 875],
                             [1326, 875]]

        for coordinate in coordinate_list_4:
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list_5 = [[173, 1000],
                             [314, 1000],
                             [378, 1000],
                             [442, 1000],
                             [580, 1000],
                             [700, 1000],
                             [830, 1000],
                             [894, 1000],
                             [1034, 1000],
                             [1160, 1000],
                             [1224, 1000]]

        for coordinate in coordinate_list_5:
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Bee walls
        coordinate_list_6 = [[173, 500],
                             [1316, 500],
                             [610, 425],
                             [960, 425],
                             [380, 625],
                             [1040, 625],
                             [1160, 750],
                             [700, 750],
                             [442, 825],
                             [830, 875],
                             [1228, 875],
                             [1034, 925],
                             [313, 925],
                             [639, 1000]]

        for coordinate in coordinate_list_6:
            wall = arcade.Sprite("bee.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Worms
        coordinate_list_7 = [[273, 575],
                             [1200, 575],
                             [173, 425],
                             [690, 430],
                             [380, 700],
                             [1040, 700],
                             [1160, 825],
                             [700, 825],
                             [377, 825],
                             [830, 950],
                             [1228, 950],
                             [1034, 1075]]

        for coordinate in coordinate_list_7:
            worm = arcade.Sprite("wormPink.png", SPRITE_SCALING)
            worm.center_x = coordinate[0]
            worm.center_y = coordinate[1]
            self.worm_list.append(worm)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.worm_list.draw()

        # Select the camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Score: {self.score} "
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)
        if len(self.worm_list) == 0:
            game = "GAME OVER"
            arcade.draw_text(game, 325, 300, arcade.color.WHITE, 20)

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
        elif len(self.worm_list) > 0:
            self.player_sprite.center_x = 0
            self.player_sprite.center_y = 0

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif len(self.worm_list) > 0:
            self.player_sprite.center_x = 0
            self.player_sprite.center_y = 0

    def on_update(self, delta_time):
        # Movement
        if len(self.worm_list) > 0:
            self.physics_engine.update()
            self.scroll_to_player()
            self.worm_list.update()
            worm_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.worm_list)

            for worm in worm_hit_list:
                worm.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(eat_sound)

    def scroll_to_player(self):
        position = self.player_sprite.center_x - self.width / 2, \
            self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
