# Just an nothing object, that can't walk path.

from Prefabs import prefab
from abc import abstractmethod


class Static(prefab.Prefab):
    """
    Static Prefab - Anything that can't be moved, or interact.
    """
    def __init__(self, color):
        super().__init__(color)

    def touch(self, env):
        """
        What will happend if the player touches this block?

        Args:
            env (game object) - the reference to the game object.
        """
        env.add_reward(-1)
