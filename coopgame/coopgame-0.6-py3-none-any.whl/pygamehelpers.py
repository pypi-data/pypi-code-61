import pygame
from coopstructs.geometry import Rectangle
from coopgame.colors import Color
from coopstructs.vectors import Vector2

def mouse_pos_as_vector() -> Vector2:
    """ Get the global coords of the mouse position and convert them to a Vector2 object"""
    pos = pygame.mouse.get_pos()
    return Vector2(pos[0], pos[1])

def draw_box(surface: pygame.Surface, rect: Rectangle, color: Color, width: int = 0):
    pygame.draw.rect(surface, color.value, (rect.x, rect.y, rect.width, rect.height), width)

def game_area_coords_from_parent_coords(parent_coords: Vector2, game_area_surface_rectangle: Rectangle) -> Vector2:
    """Converts Global Coords into coords on the game area"""
    return Vector2(parent_coords.x - game_area_surface_rectangle.x, parent_coords.y - game_area_surface_rectangle.y)
