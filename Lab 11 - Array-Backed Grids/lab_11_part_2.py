
import arcade

ROW_COUNT = 10
COLUMN_COUNT = 10
WIDTH = 60
HEIGHT = 60
MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)
            # Append a cell
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.PINK

                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

            total = 0
            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    if self.grid[row][column]:
                        total += 1
            print("There are a total of ", total, "cells selected.")

            for row in range(ROW_COUNT):
                number_cell = 0
                continuous = 0
                for column in range(COLUMN_COUNT):
                    if self.grid[row][column] == 1:
                        number_cell += 1
                        continuous += 1
                    else:
                        if continuous > 2:
                            print("There are", continuous, " continuous cells selected on Row", row)
                            continuous = 0
                if continuous > 2:
                    print("There are", continuous, " continuous cells selected on Row", row)
                print("Row", row, "has", number_cell, "cells selected")

            for column in range(COLUMN_COUNT):
                cell_numb = 0
                for row in range(COLUMN_COUNT):
                    if self.grid[row][column] == 1:
                        cell_numb += 1
                print("Column", column, "has", cell_numb, "cells selected")


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
