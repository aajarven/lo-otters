# -*- coding:utf-8 -*-

class Character:
    """ Pelissä seikkaileva hahmo.
    """

    def __init__(self, name):
        """ Creates a new character

        Args:
            name (String): name of the character
        """
        self.name = name
        self.tile = None
        self.inventory = []
        self.cards = []
        self.attack = 1
        self.defence = 1
        self.movement = 1
        self.hp = 15

    def __str__(self):
        return self.name