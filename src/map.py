# -*- coding:utf-8 -*-

class Map:
    """ Map made of tiles
    """

    def __init__(self, tiles):
        self.tiles = tiles

    # TODO mieti, mitä tehdään, jos yritetään siirtää paikkaan, johon ei voi liikkua
    def move_player(self, character, destination):
        """Moves given character to given destination

        Args:
            character (Character): character to be moved
            destination (Tile): tile to which the character is moved
        """

        character.tile.remove_player()
        destination.set_player(character)
        character.tile = destination
