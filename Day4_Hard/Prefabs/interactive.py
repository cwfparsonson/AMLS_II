# Interactive Class.

from Prefabs import prefab
from abc import abstractmethod


class Interactive(prefab.Prefab):
    """
    Anything that can be Touch, Move, Eat.
    """
    def __init__(self, color):
        super().__init__(color)

    @abstractmethod
    def touch(self, env):
        """
        What will happend if the player touches this block?

        Args:
            env (game object) - the reference to the game object.
        """
        pass 

    @abstractmethod
    def consume(self, env):
        """
        What will happend if the player decides to consum the block ?
        
        Args:
            env (game object) - the reference to the game object.
        """
        pass 


class Touchable(Interactive):
    def __init__(self, color):
        super().__init__(color)

    def touch(self, env):
        print("I am Touched")
        env.add_reward(1)

    def consume(self, env):
        print("Consumed")


class TouchableEnd(Interactive):
    def __init__(self, color):
        super().__init__(color)

    def touch(self, env):
        print("I am Touched")
        env.add_reward(1)
        env.terminate_env()

    def consume(self, env):
        print("Consumed")


class GoldObj(Interactive):
    def __init__(self, color):
        super().__init__(color)

    def touch(self, env):
        env.add_reward(10)
        env.terminate_env()

    def consume(self, env):
        print("Consumed")

