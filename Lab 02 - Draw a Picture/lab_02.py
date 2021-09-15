# Import library
import arcade

# Open window to draw
arcade.open_window(600, 800, "Drawing Example")
arcade.set_background_color((134, 199, 227))

# Get ready to draw
arcade.start_render()

# Draw grass with bumps
arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, (199, 217, 108))
arcade.draw_ellipse_filled(50, 180, 50, 50, (199, 217, 108))
arcade.draw_ellipse_filled(223, 180, 50, 50, (199, 217, 108))
arcade.draw_ellipse_filled(400, 180, 50, 50, (199, 217, 108))
arcade.draw_ellipse_filled(489, 180, 50, 50, (199, 217, 108))
arcade.draw_triangle_filled(0, 0, 470, 210, 470, 0, (199, 217, 108))
arcade.draw_triangle_filled(515, 10, 515, 210, 600, 100, (199, 217, 108))

# Outline grass
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

# Draw clouds
arcade.draw_ellipse_filled(220, 730, 80, 100, (255, 255, 255))
arcade.draw_ellipse_outline(220, 730, 80, 100, (0, 0, 0))
arcade.draw_ellipse_filled(210, 700, 100, 85, (255, 255, 255))
arcade.draw_ellipse_outline(210, 700, 100, 85, (0, 0, 0))
arcade.draw_ellipse_filled(180, 715, 115, 80, (255, 255, 255))
arcade.draw_ellipse_outline(180, 715, 115, 80,  (0, 0, 0))
arcade.draw_ellipse_filled(215, 725, 75, 90, (255, 255, 255))
arcade.draw_ellipse_filled(500, 550, 120, 80, (255, 255, 255))
arcade.draw_ellipse_outline(500, 550, 120, 80, (0, 0, 0))
arcade.draw_ellipse_filled(550, 580, 90, 50, (255, 255, 255))
arcade.draw_ellipse_outline(550, 580, 90, 50, (0, 0, 0))
arcade.draw_ellipse_filled(520, 560, 65, 50, (255, 255, 255))

# Draw sun
arcade.draw_ellipse_filled(535, 730, 80, 80, (217, 199, 82))
arcade.draw_ellipse_outline(535, 730, 80, 80, (0, 0, 0))

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
