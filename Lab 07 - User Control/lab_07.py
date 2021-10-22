""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
MOVEMENT_SPEED = 5


def draw_bird(x, y):
    arcade.draw_ellipse_filled(x, y, 20, 20, (0, 0, 0))
    arcade.draw_arc_outline(x + 20, y - 10, 40, 30, (0, 0, 0), 0, 180, 10, 1)
    arcade.draw_arc_outline(x - 20, y - 10, 40, 30, (0, 0, 0), 0, 180, 10, 1)


def draw_cloud(x, y):
    """ Draw the clouds"""
    arcade.draw_ellipse_filled(x, y, 120, 80, (255, 255, 255))
    arcade.draw_ellipse_outline(x, y, 120, 80, (0, 0, 0))
    arcade.draw_ellipse_filled(x + 50, 30 + y, 90, 50, (255, 255, 255))
    arcade.draw_ellipse_outline(x + 50, 30 + y, 90, 50, (0, 0, 0))
    arcade.draw_ellipse_filled(x, 10 + y, 65, 50, (255, 255, 255))


def draw_tree(x, y):
    arcade.draw_rectangle_filled(x, y, 20, 60, (140, 116, 95))
    arcade.draw_rectangle_outline(x, y, 20, 60, (0, 0, 0))
    arcade.draw_triangle_filled(x, y + 80, x - 30, y, x + 30, y, (118, 181, 125))
    arcade.draw_triangle_outline(x, y + 80, x - 30, y, x + 30, y, (0, 0, 0), 2)


class Bird:
    def __init__(self, position_x, position_y, change_x, change_y, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    def draw(self):
        draw_bird(self.position_x, self.position_y)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x


class Cloud:
    def __init__(self, position_x, position_y, change_x, change_y, color, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color
        self.radius = radius

    def draw(self):
        draw_cloud(self.position_x, self.position_y)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < (self.radius + 60):
            self.position_x = (self.radius + 60)

        if self.position_x > SCREEN_WIDTH - (self.radius + 95):
            self.position_x = SCREEN_WIDTH - (self.radius + 95)

        if self.position_y < (self.radius + 40):
            self.position_y = (self.radius + 40)

        if self.position_y > SCREEN_HEIGHT - (self.radius + 55):
            self.position_y = SCREEN_HEIGHT - (self.radius + 55)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.set_mouse_visible(False)
        arcade.set_background_color((134, 199, 227))

        # Create the bird
        self.bird = Bird(300, 400, 0, 0, (255, 255, 255))

        # Create the cloud
        self.cloud = Cloud(500, 575, 0, 0, (0, 0, 0), 0)

        # Create Sound
        self.error_sound = arcade.load_sound("arcade_resources_sounds_error1.wav")

    def on_draw(self):
        # Draw grass with bumps
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, (199, 217, 108))
        arcade.draw_ellipse_filled(50, 180, 50, 50, (199, 217, 108))
        arcade.draw_ellipse_filled(223, 180, 50, 50, (199, 217, 108))
        arcade.draw_ellipse_filled(400, 180, 50, 50, (199, 217, 108))
        arcade.draw_ellipse_filled(489, 180, 50, 50, (199, 217, 108))
        arcade.draw_triangle_filled(0, 0, 470, 210, 470, 0, (199, 217, 108))
        arcade.draw_triangle_filled(515, 10, 515, 210, 600, 100, (199, 217, 108))
        arcade.draw_lrtb_rectangle_filled(0, 35, 200, 200, (0, 0, 0))
        arcade.draw_lrtb_rectangle_filled(65, 208, 200, 200, (0, 0, 0))
        arcade.draw_lrtb_rectangle_filled(238, 385, 200, 200, (0, 0, 0))
        arcade.draw_lrtb_rectangle_filled(415, 448, 200, 200, (0, 0, 0))
        arcade.draw_lrtb_rectangle_filled(470, 475, 200, 200, (0, 0, 0))
        arcade.draw_lrtb_rectangle_filled(505, 515, 200, 200, (0, 0, 0))
        arcade.draw_lrtb_rectangle_filled(525, 600, 200, 200, (0, 0, 0))
        arcade.draw_lrtb_rectangle_filled(470, 470, 210, 200, (0, 0, 0))
        arcade.draw_lrtb_rectangle_filled(515, 515, 210, 200, (0, 0, 0))
        arcade.draw_line(448, 200, 470, 210, (0, 0, 0))
        arcade.draw_line(524, 200, 515, 210, (0, 0, 0))
        arcade.draw_ellipse_outline(50, 180, 50, 50, (0, 0, 0))
        arcade.draw_ellipse_outline(223, 180, 50, 50, (0, 0, 0))
        arcade.draw_ellipse_outline(400, 180, 50, 50, (0, 0, 0))
        arcade.draw_ellipse_outline(489, 180, 50, 50, (0, 0, 0))
        arcade.draw_lrtb_rectangle_filled(0, 600, 199, 0, (199, 217, 108))

        # Draw Snoopy's dog house
        arcade.draw_lrtb_rectangle_filled(200, 385, 300, 100, (240, 46, 46))
        arcade.draw_lrtb_rectangle_outline(200, 385, 300, 100, (0, 0, 0), 2)
        arcade.draw_triangle_filled(150, 250, 180, 425, 400, 425, (240, 46, 46))
        arcade.draw_triangle_filled(435, 250, 405, 425, 180, 425, (240, 46, 46))
        arcade.draw_triangle_filled(150, 250, 300, 425, 435, 250, (240, 46, 46))
        arcade.draw_line(150, 250, 435, 250, (0, 0, 0), 2)
        arcade.draw_line(150, 250, 180, 425, (0, 0, 0), 2)
        arcade.draw_line(180, 425, 405, 425, (0, 0, 0), 2)
        arcade.draw_line(405, 425, 435, 250, (0, 0, 0), 2)
        arcade.draw_line(200, 146.67, 385, 146.67, (0, 0, 0), 2)
        arcade.draw_line(200, 203.34, 385, 203.34, (0, 0, 0), 2)
        arcade.draw_triangle_filled(150, 250, 155, 245, 175, 250, (0, 0, 0))
        arcade.draw_triangle_filled(435, 250, 430, 245, 175, 250, (0, 0, 0))
        arcade.draw_lrtb_rectangle_filled(155, 430, 250, 245, (0, 0, 0))
        arcade.draw_line(172, 380, 413, 380, (0, 0, 0), 2)
        arcade.draw_line(159, 310, 425, 310, (0, 0, 0), 2)

        # Draw sun
        arcade.draw_ellipse_filled(535, 730, 80, 80, (217, 199, 82))
        arcade.draw_ellipse_outline(535, 730, 80, 80, (0, 0, 0))

        draw_cloud(75, 700)
        draw_cloud(300, 700)

        draw_tree(100, 225)
        self.bird.draw()
        self.cloud.draw()

    def update(self, delta_time):
        self.bird.update()
        self.cloud.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.cloud.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.cloud.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.cloud.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.cloud.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.cloud.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.cloud.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        self.bird.position_x = x
        self.bird.position_y = y


def main():
    window = MyGame()
    arcade.run()


main()
