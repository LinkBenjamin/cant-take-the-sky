import pygame
import logging
import os

from .base_scene import BaseScene
from app.etc.utils import safe_load_int

class MainMenu(BaseScene):
    def __init__(self, screen):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.screen = screen
        self.bg_color = [60,10,8]
        self.text_color = [255,255,0]

        self.font_size = 60
        self.font = pygame.font.Font('assets/fonts/papyrus/papyrus.ttc', self.font_size)
        self.title_font = pygame.font.Font('assets/fonts/corabael/corabael_regular.ttf', self.font_size + 20)

        self.screen_width = safe_load_int(os.environ.get("SCREEN_WIDTH"), self.logger)
        self.screen_height = safe_load_int(os.environ.get("SCREEN_HEIGHT"), self.logger)

        self.menu_items = [
            {'label': 'New Game', 'action':'new'},
            {'label': 'Load Game', 'action':'load'},
            {'label': 'Quit', 'action':'quit'}
        ]
        self.buttons = []
        self._setup_buttons()

        self.selection = ""

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.selection = 'quit'
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn in self.buttons:
                    if btn["rect"].collidepoint(event.pos):
                        self.logger.debug(f"Menu selection: {btn['action']}")
                        self.selection = btn['action']

    def update(self):
        match self.selection:
            case 'quit':
                self.on_quit_selected()
            case 'new':
                self.on_new_selected()
            case 'load':
                self.on_load_selected()
    

    def draw(self):
        self.screen.fill(self.bg_color)

        title_surf = self.title_font.render(os.environ.get('GAME_NAME'),True, self.text_color)
        title_rect = title_surf.get_rect(center=(self.screen_width // 2, 100))
        self.screen.blit(title_surf, title_rect)

        for btn in self.buttons:
            mouse_pos = pygame.mouse.get_pos()
            color = (200,200,200) if btn['rect'].collidepoint(mouse_pos) else self.text_color

            text_surf = self.font.render(btn["label"], True, color)
            self.screen.blit(text_surf, btn["rect"])
        
        pygame.display.flip()

    def _setup_buttons(self):
        start_y = 200
        padding = 75

        for i, item in enumerate(self.menu_items):
            text_surf = self.font.render(item['label'], True, self.text_color)
            rect = text_surf.get_rect(center=(self.screen_width // 2, start_y + (i * padding)))
            self.buttons.append({"rect":rect, "action": item["action"], "label": item["label"]})

    def on_quit_selected(self):
        self.logger.info("Quit Selected.  Exiting...")
        self.switch_to(None)

    def on_new_selected(self):
        self.logger.info("New Game Selected.")
        # self.switch_to( new game thing )

    def on_load_selected(self):
        self.logger.info("Load Game Selected.")
        # self.switch_to( load game thing )