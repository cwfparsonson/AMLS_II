# Build a game representation from ascii art defined by user.
from Prefabs import exceptions, player
import itertools
from copy import deepcopy
import game
import numpy as np


class AsciiMapException(Exception):
    pass


class ObjectInfoException(Exception):
    pass


def build_game(ascii_art, objs_info, obj_size):
    """
    Create the game object from ascii art and objects_information by
    creating difference layers, and pass it to the initilizer.

    Args:
        ascii_art (list of strings)
            The art for the game, must be in rectangle
            (meaning that the lenth of inside list shoud be the same)
            where, the empty string means nothing and the labeled characters
            are representing the object in game.

        objects_information (dictionary)
            We map the characters to prefab object, so that we can easily
            define their colors or behavior.

    Return:
        game (Game object) - Game object created by game class.

    Raises:
        ValueError - When the map is not a rectangle.
        AttributeError - object information isn't contain some
            characters from ascii_art.

    Example:
        Ascii Art

        ['########'
        ,'#      #'
        ,'#      #'
        ,'#   P  #'
        ,'#      #'
        ,'#      #'
        ,'#      #'
        ,'########']

        Object information
        {'P': Player(), '#': Wall()}

    """

    # Testing for the property of the map

    if not all(len(r) == len(ascii_art[0]) for r in ascii_art):
        raise AsciiMapException("The map is not consistent.")

    if ascii_art == []:
        raise AsciiMapException("The map is empty.")

    if not bool(objs_info):
        raise ObjectInfoException("The object information is empty.")

    # Get all the objects
    all_obs = list(set(itertools.chain.from_iterable(ascii_art)))
    all_obs = [o for o in all_obs if not o == ' ']

    if len(all_obs) < len(objs_info.keys()):
        raise ObjectInfoException("Some of the objects are not in the map.")

    if not all(o in objs_info for o in all_obs):
        raise ObjectInfoException("There is no information for the object.")

    # Rules for dividing the layers.
    # Static, Interactive - no matter the object created should be in the same layers (layer 0)
    # Difference Player should have difference layers. (layer 1 onward)

    map_size = (len(ascii_art[0]), len(ascii_art))
    objs_lookup = dict()
    player_list = []

    for y, row in enumerate(ascii_art):
        for x, obj in enumerate(row):
            if obj != ' ':
                obj_created = deepcopy(objs_info[obj])
                obj_created.location = (x, y)
                obj_created.size = obj_size

                objs_lookup[(x, y)] = [obj_created]

    game_obj = game.Game(objs_lookup, map_size)
    return game_obj


def build_random_game(grid_size, objs_info, obj_size, number_objs = 1):
    """
    Create the game object from ascii art and objects_information by
    creating difference layers, and pass it to the initilizer.

    Args:
        ascii_art (list of strings)
            The art for the game, must be in rectangle
            (meaning that the lenth of inside list shoud be the same)
            where, the empty string means nothing and the labeled characters
            are representing the object in game.

        objects_information (dictionary)
            We map the characters to prefab object, so that we can easily
            define their colors or behavior.

    Return:
        game (Game object) - Game object created by game class.

    Raises:
        ValueError - When the map is not a rectangle.
        AttributeError - object information isn't contain some
            characters from ascii_art.

    Example:
        Ascii Art

        ['########'
        ,'#      #'
        ,'#      #'
        ,'#   P  #'
        ,'#      #'
        ,'#      #'
        ,'#      #'
        ,'########']

        Object information
        {'P': Player(), '#': Wall()}

    """

    # Testing for the property of the map

    if grid_size == 0:
        raise AsciiMapException("The map is empty.")

    if not bool(objs_info):
        raise ObjectInfoException("The object information is empty.")

    walls = []
    walls.extend(zip([0]*grid_size,range(grid_size))) # upper wall
    walls.extend(zip(range(1,grid_size-1), [0]*(grid_size-1))) # lower wall
    walls.extend(zip(range(1,grid_size-1), [grid_size-1]*(grid_size-1))) # left wall
    walls.extend(zip([grid_size-1]*grid_size,range(grid_size))) # right wall

    map_size = (grid_size, grid_size)

    game_obj = game.Game(None, map_size, walls=walls, grid_size=grid_size, number_objs=number_objs,
                 obj_size=obj_size, objs_info=objs_info)
    return game_obj
