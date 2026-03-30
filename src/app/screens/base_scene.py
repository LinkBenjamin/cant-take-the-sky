'''
    BaseScene is an Abstract class defining a scene in the game.
'''
import logging

from abc import ABC, abstractmethod

class BaseScene(ABC):
    def __init__(self):
        self.next_scene = ""
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def handle_events(self, events):
        """Child classes MUST handle their own input."""
        pass

    @abstractmethod
    def update(self):
        """Child classes MUST handle their own logic."""
        pass

    @abstractmethod
    def draw(self):
        """Child classes MUST handle their own rendering."""
        pass

    def switch_to(self, next_scene):
        """This is a helper, so it doesn't need to be abstract."""
        self.logger.debug(f"switch_to( {next_scene} ) called.")
        self.next_scene = next_scene