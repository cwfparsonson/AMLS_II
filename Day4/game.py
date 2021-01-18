# This file contain the defintion of the game class.

import numpy as np
import matplotlib.pyplot as plt
from Prefabs import exceptions, player, static, interactive
import warnings
import copy


class Game(object):
    """
    Game Enviroment Class

    Attributes:
        objs_lookup (dict) - Getting the object based on the location.
        map_size (2 element tuple) - the size of the map (w x h)
    """
    def __init__(self, objs_lookup, map_size, walls=None, grid_size=None, number_objs=None,
                 obj_size=None, objs_info=None):
        if objs_lookup is not None:
            self.objs_lookup = objs_lookup
            self.random_init = False
        else:
            self.random_init = True
            self.walls = walls
            self.grid_size = grid_size
            self.number_objs = number_objs
            self.objs_info = objs_info
            self.obj_size = obj_size
            self.objs_lookup = self.build_objs_lookup()

        self.map_size = map_size

        # Just get the size of the object in the scene
        self._obj_size = list(self.objs_lookup.items())[0][1][0].size

        # Just create an object of the same size.
        _empty_tile = static.Static((255, 255, 255))
        _empty_tile.size = self._obj_size

        self.empty_tile_numpy = _empty_tile.numpy_tile
        self.reward = 0
        self.terminate = False
        self.steps_taken = 0

        # For reset the game - safe the start state
        self._start_state = copy.deepcopy(self.objs_lookup)
        
        # just to init everything 
        self._list_players = self.get_list_players()

        self._MAX_STEPS = 100

    @property
    def objs_lookup(self):
        return self._objs_lookup

    @objs_lookup.setter
    def objs_lookup(self, value):
        # Checking that there is no object missing - TODO - Not sure
        # all_objs_new = set([sv for sv in v for _, v in value.items()])
        # objs_new = set([sv for sv in v for _, v in self._objs_lookup])
        #
        # if objs_new != all_objs_new:
        #     exceptions.ObjectMissingException("There is some object missing!!")
        
        self._objs_lookup = value

    def build_objs_lookup(self):
        objects = []

        for o in range(self.number_objs):
            object_x = np.random.randint(self.grid_size)
            object_y = np.random.randint(self.grid_size)
            obj = (object_x, object_y)

            while (obj in self.walls) or (obj in objects):
                object_x = np.random.randint(self.grid_size)
                object_y = np.random.randint(self.grid_size)
                obj = (object_x, object_y)
            objects.append(obj)

        player_x = np.random.randint(self.grid_size)
        player_y = np.random.randint(self.grid_size)
        player = (player_x, player_y)
        while (player in self.walls) or (player in objects):
            player_x = np.random.randint(self.grid_size)
            player_y = np.random.randint(self.grid_size)
            player = (player_x, player_y)

        # Rules for dividing the layers.
        # Static, Interactive - no matter the object created should be in the same layers (layer 0)
        # Difference Player should have difference layers. (layer 1 onward)

        map_size = (self.grid_size, self.grid_size)
        objs_lookup = dict()

        for o in self.walls:
            obj = '#'
            obj_created = copy.deepcopy(self.objs_info[obj])
            obj_created.location = o
            obj_created.size = self.obj_size
            objs_lookup[o] = [obj_created]

        for o in objects:
            obj = 'I'
            obj_created = copy.deepcopy(self.objs_info[obj])
            obj_created.location = o
            obj_created.size = self.obj_size
            objs_lookup[o] = [obj_created]

        obj = 'P'
        obj_created = copy.deepcopy(self.objs_info[obj])
        obj_created.location = player
        obj_created.size = self.obj_size
        objs_lookup[player] = [obj_created]

        return objs_lookup

    def get_list_players(self):
        """Return list of players, guaruntee that I will not be None"""
        
        players = []
        for key, value in self.objs_lookup.items():
            for v in value: 
                if isinstance(v, player.Player):
                    players.append(v)

        if len(players) == 0:
            warnings.warn("There is no player in the game. You can't call step method")
        
        for p in players:
            p.game = self

        return players
 
    @property
    def reward(self):
        """The reward of the player right now"""
        return self._reward

    @reward.setter
    def reward(self, value):
        """Setting up the reward"""

        # Check for the conditions 
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("The reward should be int, or float")

        self._reward = value
    
    @property
    def terminate(self):
        return self._terminate

    @terminate.setter
    def terminate(self, value):
        if not isinstance(value, bool):
            raise TypeError("Termination should be boolean")
        self._terminate = value

    def add_reward(self, amount):
        """
        When we call this function add the total reward by the ammount

        Args:
            1. amount (int) - the amount of the reward we have to add 

        Raises:
            TypeError - if the amount is not int or float.
        """
        self.reward += amount

    def terminate_env(self):
        """
        Just mark the enviroment as termianted.
        """
        self.terminate = True
    
    def step(self, action):
        """
        Given an action what should we do ?
        We just going to call the action of the players
        For now, we will consider only single player first.

        Args:
            1. action(int) - the action for what player we want to act.

        Return:
            1. Observation (numpy image) - the observation of the map.
            2. Reward (int) - TODO.
        """
        if self.terminate:
            raise exceptions.EnvTerminateException("The env is terminated.")

        if len(self._list_players) > 1:
            warnings.warn("There is more than one player - \
                            Not supporting right now, might causes unwanted behavior.")
        # Everytime the step is called we are going to reset the reward 
        self.reward = 0

        self.steps_taken += 1

        # Suppose p is 1 element list.
        for player in self._list_players:
            player.step(action)

        if self.steps_taken >= self._MAX_STEPS:
            self.terminate_env()

        rendered_map = self.render_map().sum(axis=2) / 3.
        return np.reshape(rendered_map, [rendered_map.shape[0], rendered_map.shape[1], 1]), self.reward, self.terminate
    
    def _change_player_pos(self, player_location, next_location):
        """
        This will change the position of the player no matter what

        Args:
            1. player_location (2 element tuple) - 
                the current location of the player
            2. next_location (2 element tuple) - 
                the new location of the player.
        """
        # We have to check that there aren't any overlap player

        if len(self.objs_lookup[player_location]) < 2:
            # First Remove the player at that location.
            player_obj = self.objs_lookup.pop(player_location)
            self.objs_lookup[next_location] = player_obj

        else:
            # If there are more than one objects in the current location 
            # Then we have to remore the last one which is the player. 
            player_obj = self.objs_lookup[player_location].pop()
            self.objs_lookup[next_location] = [player_obj]
            
        # Change it to the next location.

    def _move_player(self, player_location, next_location):
        """
        Given the plater location and its next location
        change the lookup table and then return the next location

        Args:
            1. player_location (2 elements tuple) -
                the current location of the player.
            2. next_location (2 elements tuple) -
                the next location we want to move the player to

        Return
            1. next location (2 element tuple)
        """

        location = player_location
        
        # Update the lookup table.
        # If there is nothing, then proceed the move.
        if not next_location in self.objs_lookup:
            self._change_player_pos(player_location, next_location) 
            location = next_location 
        else:
            # If next is the static - then you can't move.

            # Warning - we will accessing just the first element.
            if isinstance(self.objs_lookup[next_location][0],
                                    static.Static):
                next_object = self.objs_lookup[next_location][0]
                next_object.touch(self)
            else:

                # get the content
                player_obj = self.objs_lookup.pop(player_location)[0]
                
                next_object = self.objs_lookup[next_location][0]

                # just in case 
                if isinstance(next_object, interactive.Interactive):
                    next_object.touch(self)

                content = self.objs_lookup[next_location]
                content.append(player_obj)  
                
                location = next_location
                
        return location

    def move_north(self, player_location):
        """
        Move the player to north direction.
        And return the location of the player + update the lookup table.

        Args:
            1. player_location(tuple of 2 elements) -
                the player location right now

        Return:
            1. player_new_location (tuple of 2 elements) -
                the location of the player after it moves upward.
        """
        next_possible_location = (player_location[0], player_location[1]-1)
        return self._move_player(player_location, next_possible_location)

    def move_east(self, player_location):
        """
        Move the player to east direction.
        And return the location of the player + update the lookup table.

        Args:
            1. player_location(tuple of 2 elements) -
                the player location right now

        Return:
            1. player_new_location (tuple of 2 elements) -
                the location of the player after it moves upward.
        """

        next_possible_location = (player_location[0]+1, player_location[1])

        return self._move_player(player_location, next_possible_location)

    def move_south(self, player_location):
        """
        Move the player to south direction.
        And return the location of the player + update the lookup table.

        Args:
            1. player_location(tuple of 2 elements) -
                the player location right now

        Return:
            1. player_new_location (tuple of 2 elements) -
                the location of the player after it moves upward.
        """

        next_possible_location = (player_location[0], player_location[1]+1)
        return self._move_player(player_location, next_possible_location)

    def move_west(self, player_location):
        """
        Move the player to west direction.
        And return the location of the player + update the lookup table.

        Args:
            1. player_location(tuple of 2 elements) -
                the player location right now

        Return:
            1. player_new_location (tuple of 2 elements) -
                the location of the player after it moves upward.
        """
        next_possible_location = (player_location[0]-1, player_location[1])
        return self._move_player(player_location, next_possible_location)

    def render_map(self):
        """
        Render the map y returning the numpy array

        Return
            Image (numpy array) - the entire map rendered to an image.
        """
        size_x, size_y = self.map_size
        map_array = []

        for x in range(size_x):
            row = []
            for y in range(size_y):
                if (x, y) in self.objs_lookup:
                    # Since we store it in list. So display the first object first.
                    row.append(self.objs_lookup[(x,y)][0].numpy_tile)
                else:
                    row.append(self.empty_tile_numpy)
            # Have to reverse for the reshape to work.
            map_array.append(np.hstack(row))

        # Have to reverse for the reshape to work.
        image = np.array(map_array).reshape(size_x * self._obj_size,
                                                size_y * self._obj_size, 3)

        assert all(len(map_array[0]) == len(r) for r in map_array)

        # Flipping the image.
        return np.flip(np.rot90(image), 0)

    def display_map(self):
        """
        Display map of the game.
        """
        plt.imshow(self.render_map())
        plt.show()

    def reset(self):
        """
        Reset Everything.
        
        Return:
            The first scene
        
        Warns:
            If the game is not terminated, we shoud warn the user, first
        """
        if not self.terminate:
            warnings.warn("The game hasn't terminated for reset")

        if not self.random_init:
            self.objs_lookup = copy.deepcopy(self._start_state)
        else:
            self.objs_lookup = self.build_objs_lookup()

        # After reset it is not terminated
        self.terminate = False
        self.steps_taken = 0
        self._list_players = self.get_list_players()

        rendered_map = self.render_map().sum(axis=2) / 3.
        return np.reshape(rendered_map, [rendered_map.shape[0], rendered_map.shape[1], 1])
