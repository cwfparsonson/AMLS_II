# Player Prefab so that we can control it.
# from Prefabs import player, prefab
from Prefabs import prefab, exceptions
from abc import ABC, abstractmethod


class Player(prefab.Prefab):
    """
    Player Abstract Class Used to define player's behavior.

    Attributes -
        Similar to the Prefab but having
        game (Game object) - the reference to the game object,
            can't be used until it is initalized

    Raises -
        exceptions.NotInitalizedException -
            Trying to access the _game variable without initilize it.
            OR Trying to play the game with initilize the game object.
    """
    def __init__(self, color):
        super().__init__(color)
        self._game = None

    @property
    def game(self):
        """Get the game object, will initilized this afterward"""
        if self._game is None:
            raise exceptions.NotInitalizedException("Game haven't been initilized")

        return self._game

    @game.setter
    def game(self, value):
        """Get the reference of the game, will initilized this afterward"""
        self._game = value

    @abstractmethod
    def step(self, action):
        """
        Given Action what should the player do?

        Arg:
            1. action (int) - The action we want the player to do.
        """
        pass

    def _north(self):
        """
        Move the player to the north direction.
        """
        if self._game is None:
            raise exceptions.NotInitalizedException("Game haven't been initilized")

        # Get the next location after moving to the north.
        # print(self)
        self.location = self.game.move_north(self.location)

    def _east(self):
        """
        Move the player to the east direction.
        """
        if self._game is None:
            raise exceptions.NotInitalizedException("Game haven't been initilized")

        # Get the next location after moving to the north.
        self.location = self.game.move_east(self.location)

    def _south(self):
        """
        Move the player to the south direction.
        """
        if self._game is None:
            raise exceptions.NotInitalizedException("Game haven't been initilized")

        # Get the next location after moving to the north.
        self.location = self.game.move_south(self.location)

    def _west(self):
        """
        Move the player to the west direction.
        """
        if self._game is None:
            raise exceptions.NotInitalizedException("Game haven't been initilized")

        # Get the next location after moving to the north.
        self.location = self.game.move_west(self.location)


class NormalPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    def step(self, action):
        if action == 0:
            self._north()
        elif action == 1:
            self._east()
        elif action == 2:
            self._south()
        elif action == 3:
            self._west()
