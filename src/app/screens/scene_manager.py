import pygame
import logging

from app.screens.main_menu import MainMenu
from app.screens.about_page import AboutPage

class SceneManager:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.scenes = {
            "main_menu": MainMenu,
            "about": AboutPage
        }
        self.active_scene = None
        self.change_scene("main_menu")

    def change_scene(self, name):
        if name:
            self.logger.debug(f"Changing scene to {name}")
            self.active_scene = self.scenes[name](self.screen,self)
        else:
            self.active_scene = None

    def run(self):
        while self.active_scene is not None:
            # 1. Get Events once per frame
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.active_scene = None # Exit the loop
                    return

            # 2. Let the active scene handle its specific logic
            if self.active_scene is not None:
                self.active_scene.handle_events(events)
                self.active_scene.update()
            
            # 3. Draw
                self.active_scene.draw()
                pygame.display.flip()

            # 4. Check if the scene wants to switch
                if self.active_scene.next_scene != "":
                    self.change_scene(self.active_scene.next_scene)
            
                self.clock.tick(60)