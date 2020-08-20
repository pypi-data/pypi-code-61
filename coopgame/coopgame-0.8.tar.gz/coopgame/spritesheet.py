# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

# Additional notes
# - Further adaptations from https://www.pygame.org/wiki/Spritesheet
# - Cleaned up overall formatting.
# - Updated from Python 2 -> Python 3.

import pygame
from coopstructs.vectors import Vector2


class SpriteSheet:

    def __init__(self, filename, pixel_width, pixel_height):
        self.pixel_width = pixel_width
        self.pixel_height = pixel_height

        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

        self.n_images_in_row = self.sheet.get_width() // self.pixel_width
        self.n_images_in_column = self.sheet.get_height() // self.pixel_height

    def image_at(self, pos: Vector2, colorkey = None, x_margin=0, x_padding=0,
            y_margin=0, y_padding=0):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        rectangle = (pos.x * self.pixel_width, pos.y * self.pixel_height, self.pixel_width, self.pixel_height)
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def image_at_rect(self, rectangle, colorkey = None):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey = None):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at_rect(rect, colorkey) for rect in rects]


    def load_row_strip(self, row, colorkey = None, x_margin=0, x_padding=0,
                         y_margin=0, y_padding=0):
        grid_images = self.load_grid_images(x_margin=x_margin, x_padding=x_padding,
                         y_margin=y_margin, y_padding=y_padding, colorkey=colorkey)
        return grid_images[row]

    def load_column_strip(self, column, colorkey = None, x_margin=0, x_padding=0,
                         y_margin=0, y_padding=0):
        grid_images = self.load_grid_images(x_margin=x_margin, x_padding=x_padding,
                         y_margin=y_margin, y_padding=y_padding, colorkey=colorkey)
        return [row[column] for row in grid_images]

    def load_grid_images(self, x_margin=0, x_padding=0,
                         y_margin=0, y_padding=0, colorkey = None):
        """Load a grid of images.
        x_margin is space between top of sheet and top of first row.
        x_padding is space between rows.
        Assumes symmetrical padding on left and right.
        Same reasoning for y.
        Calls self.images_at() to get list of images.
        """
        sheet_rect = self.sheet.get_rect()
        sheet_width, sheet_height = sheet_rect.size

        # To calculate the size of each sprite, subtract the two margins,
        #   and the padding between each row, then divide by num_cols.
        # Same reasoning for y.
        x_sprite_size = (sheet_width - 2 * x_margin
                         - (self.n_images_in_row - 1) * x_padding) / self.n_images_in_row
        y_sprite_size = (sheet_height - 2 * y_margin
                         - (self.n_images_in_column - 1) * y_padding) / self.n_images_in_column

        grid_images = []
        for row_num in range(self.n_images_in_column):
            grid_images.append([])
            for col_num in range(self.n_images_in_row):
                # Position of sprite rect is margin + one sprite size
                #   and one padding size for each row. Same for y.
                x = x_margin + col_num * (x_sprite_size + x_padding)
                y = y_margin + row_num * (y_sprite_size + y_padding)
                sprite_rect = x, y, x_sprite_size, y_sprite_size
                grid_images[row_num].append(self.image_at_rect(sprite_rect, colorkey=colorkey))

        return grid_images