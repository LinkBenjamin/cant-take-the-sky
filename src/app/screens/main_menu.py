'''
The Main Menu of our game
'''
import logging
import os
import pygame
from app.etc.utils import safe_load_int
from app.screens.base_scene import BaseScene\

class MainMenu(BaseScene):
    '''The MainMenu class'''
    def __init__(self, screen, manager):
        super().__init__()

        self.scene_manager = manager

        pygame.mixer.music.load('assets/music/Firefly.mp3')
        pygame.mixer.music.play(loops=0, fade_ms=2000)
        pygame.mixer.music.set_volume(0.05)

        self.logger = logging.getLogger(self.__class__.__name__)
        self.screen = screen
        self.bg_color = [60,10,8]
        self.text_color = [255,255,0]

        self.screen_width = safe_load_int(os.environ.get("SCREEN_WIDTH"), self.logger)
        self.screen_height = safe_load_int(os.environ.get("SCREEN_HEIGHT"), self.logger)

        self.bg_image = pygame.image.load('assets/images/menu_serenity/serenity.jpg').convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_height))

        self.font_size = 60
        self.font = pygame.font.Font('assets/fonts/papyrus/papyrus.ttc', self.font_size)
        self.title_font = pygame.font.Font('assets/fonts/corabael/corabael_regular.ttf', self.font_size + 20)

        self.menu_items = [
            {'label': 'New Game', 'action':'new'},
            {'label': 'Load Game', 'action':'load'},
            {'label': 'About', 'action':'about'},
            {'label': 'Quit', 'action':'quit'}
        ]
        self.buttons = []
        self._setup_buttons()

        self.selection = None

    def handle_events(self, events):
        '''What to do when the user interacts with the menu'''
        for event in events:
            if event.type == pygame.QUIT:
                self.selection = 'quit'

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn in self.buttons:
                    if btn["rect"].collidepoint(event.pos):
                        self.logger.debug("Menu selection: %s", btn['action'])
                        self.selection = btn['action']

    def update(self):
        '''What to do when the screen updates'''
        if self.selection:
            self.on_selection(self.selection)

    def draw(self):
        '''How to redraw the screen'''
        self.screen.blit(self.bg_image, (0, 0))

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

    def on_selection(self, action):
        '''Handle a selection from the menu'''
        self.logger.info("%s Selected.", action)
        pygame.mixer.music.fadeout(1500)
        match action:
            case 'quit':
                self.switch_to(None)
            case 'about':
                self.switch_to("about")
                self.selection = ''
            # case 'new':
            # case 'load':
