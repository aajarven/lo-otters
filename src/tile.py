# -*- coding:utf-8 -*-

class Tile:
    """ Tile that can hold for example a character, a box or a trap. Map consists of tiles.
    """

    def __init__(self, x: int, y: int):
        """Creates a new tile.

        Args:
            x (int): x coordinate of tile
            y (int): y coordinate of tile
        """
        self.coordinates = (x, y)
        self.trap = None
        self.character = None
        self.monster = None
        self.box = None

    def is_walkable(self):
        """ Returns True if a player or a monster can walk on this tile, otherwise False.
        """
        if self.trap == None and self.character == None and self.monster == None:
            return True
        else:
            return False

    def remove_player(self):
        self.character = None

    def set_player(self, character):
        if self.character != None:
            raise TileReserved("Character " + str(character) + " cannot be moved to tile " + str(self) + " because "
                               + "tile is already occupied by character " + str(self.character))
        else:
            self.character = character


class TileReserved(Exception):
    pass
