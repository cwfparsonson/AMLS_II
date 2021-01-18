# Base Case for the prefab objects in the game

from abc import ABC, abstractmethod
import numpy as np

import matplotlib.pyplot as plt
from Prefabs import exceptions

class Prefab(ABC):
    """
    Base Class for all prefabs(object) in the game.

    Attributes:
        color (3 elements tuple of ints) - the RGB code for the color.
            (range is 0-255 not 0-1)
        size (int) - the size of the pixel tile.
        _location (2 element tuples) - the location of that prefab.
            It will be initalized while creating the game.
            You can't accesss it unless it is initalized

    Raises:
        TypeError -
            When the color type is not 3 elements integer tuple.
            When size is not int and not positive.

        exceptions.NotInitalizedException-
            When we try to access the location without initalized it first.
    """
    def __init__(self, color):
        self.color = color

        self._size = None
        self._location = None

    @property
    def location(self):
        """
        Get the location of the player.
        Noted that it will in initilized when create the map

        Return
            1. location (2 elements tuple) - the location of the player.
        """
        if self._location is None:
            raise exceptions.NotInitalizedException("Location haven't been initilized")
        
        return self._location

    @location.setter
    def location(self, value):
        """
        Set the location of the player.
        Noted that it will in initilized when create the map

        Args:
            1. value (2 elements tuple) - the location of the player.

        Raises:
            TypeError - When the value contains non-integer values or
                the size of the tuple is not 2
        """

        # Similar to prefab
        if not isinstance(value, tuple):
            raise TypeError("Expect 2 elements tuple - got " +
                                    value.__class__.__name__)
        else:
            if len(value) != 2:
                raise TypeError("Expect 2 elements tuple - got " +
                                    str(len(value)) + " elements tuple.")
            elif not all(isinstance(c, int) for c in value):
                raise TypeError("Expect 2 elements tuple of type int")
        
        self._location = value


    @property
    def color(self):
        """Getter method for the color."""
        return self._color

    @color.setter
    def color(self, value):
        """
        Setter method for the color

        Args:
            value (3 element tuple) - the RGB code for the color.

        Raises:
            TypeError -
                If the value is not a tuple.
                If the size of the tuple is not 3.
                If the tuple doesn't contain integer.

            ValueError -
                If the value is less than 0 or more than 255
        """
        if not isinstance(value, tuple):
            raise TypeError("Expect 3 elements tuple - got " +
                                    value.__class__.__name__)
        else:
            if len(value) != 3:
                raise TypeError("Expect 3 elements tuple - got " +
                                    str(len(value)) + " elements tuple.")

            elif not all(isinstance(c, int) for c in value):
                raise TypeError("Expect 3 elements tuple of type int")

            elif not all(0 <= c <= 255 for c in value):
                raise ValueError("Color can't be more than 255 or less than 0")


        self._color = value

    @property
    def size(self):
        """Getter method for the size"""
        if self._size is None:
            raise exceptions.NotInitalizedException("The size isn't initilized.")
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter method for the size

        Args:
            value (positive int) - the size of the tile in the grid.

        Raises:
            TypeError - When the size is not int.
            ValueError - When the size is not positive.
        """

        if not isinstance(value, int):
            raise TypeError("Expect size to be int - got " +
                                value.__class__.__name__)
        else:
            if value <= 0:
                raise ValueError("Expect size to be positive int")

        self._size = value

    @property
    def numpy_tile(self):
        """
        Create the numpy tile for creating the grid world

        Return:
            numpy tile (size x size x 3 numpy array) - numpy tile
        """
        one_pixel = np.array([c/255 for c in self.color])
        tile_pixel = [[one_pixel for _ in range(self.size)]
                                    for _ in range(self.size)]
        return np.array(tile_pixel, dtype=np.float32)

    def _display_tile(self):
        """
        Display the tile. Use for debug only.
        """
        plt.imshow(self.numpy_tile)
        plt.show()

    def __eq__(self, other):
        """This is how we compare 2 prefabs together."""
        return type(other) == type(self) \
            and other.color == self.color \
            # and other.location == self.location \
            # and other.size == self.size
