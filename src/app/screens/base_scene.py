'''
    BaseScene is an Abstract class defining a scene in the game.
'''
import logging

from abc import ABC, abstractmethod

class BaseScene(ABC):
    '''
    BaseScene defines a 'next_scene' variable and a switch_to method, 
    while leaving the other parts of a scene to be abstracted.
    '''
    def __init__(self):
        self.next_scene = ""
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def handle_events(self, events):
        """Child classes MUST handle their own input."""

    @abstractmethod
    def update(self):
        """Child classes MUST handle their own logic."""

    @abstractmethod
    def draw(self):
        """Child classes MUST handle their own rendering."""

    def switch_to(self, next_scene):
        """This is a helper, so it doesn't need to be abstract."""
        self.logger.debug("switch_to( %s ) called.", next_scene)
        self.next_scene = next_scene
