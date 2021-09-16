# Import library
import arcade

screen_width = 600
screen_height = 800


def draw_cloud(x, y):
    """ Draw the clouds"""
    arcade.draw_ellipse_filled(x, y, 120, 80, (255, 255, 255))
    arcade.draw_ellipse_outline(x, y, 120, 80, (0, 0, 0))
    arcade.draw_ellipse_filled(x + 50, 30 + y, 90, 50, (255, 255, 255))
    arcade.draw_ellipse_outline(x + 50, 30 + y, 90, 50, (0, 0, 0))
    arcade.draw_ellipse_filled(x, 10 + y, 65, 50, (255, 255, 255))


def draw_bird(x, y):
    arcade.draw_ellipse_filled(x, y, 20, 20, (0, 0, 0))
    arcade.draw_arc_outline(x + 20, y - 10, 40, 30, (0, 0, 0), 0, 180, 10, 1)
    arcade.draw_arc_outline(x - 20, y - 10, 40, 30, (0, 0, 0), 0, 180, 10, 1)


def draw_tree(x, y):
    arcade.draw_rectangle_filled(x, y, 20, 60, (140, 116, 95))
    arcade.draw_rectangle_outline(x, y, 20, 60, (0, 0, 0))
    arcade.draw_triangle_filled(x, y + 80, x - 30, y, x + 30, y, (118, 181, 125))
    arcade.draw_triangle_outline(x, y + 80, x - 30, y, x + 30, y, (0, 0, 0), 2)


def main():
    arcade.open_window(screen_width, screen_height, "Drawing Example")
    arcade.set_background_color((134, 199, 227))
    arcade.start_render()

    # Draw grass with bumps
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
    draw_cloud(500, 575)

    draw_bird(500, 500)
    draw_bird(100, 550)

    draw_tree(100, 225)

    # Finish drawing and run
    arcade.finish_render()
    arcade.run()


main()
