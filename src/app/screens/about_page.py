'''
About Page
This is a Screen inheriting from BaseScene, and it displays a brief
message as well as a button to return to the main menu.
'''

import pygame

from app.screens.base_scene import BaseScene

class AboutPage(BaseScene):
    '''AboutPage is a simple screen that displays a message and an OK button'''
    def __init__(self, screen, manager):
        super().__init__()
        self.screen = screen
        self.scene_manager = manager
        self.font = pygame.font.SysFont('Arial', 24)
        self.button_font = pygame.font.SysFont('Arial', 32)

        # The paragraph text split into a list of strings
        self.text_lines = [
            "This game was built using Pygame.",
            "I'm not trying to infringe on any",
            "copyrights or make any money, I'm just",
            "a browncoat who wants to celebrate",
            "the greatest TV show ever.",
            "",
            "So don't sue me, y'all. It's just",
            "some fun!"
        ]

        # Define the "OK" button (Centered at bottom)
        self.button_rect = pygame.Rect(0, 0, 100, 50)
        self.button_rect.center = (self.screen.get_width() // 2, self.screen.get_height() - 80)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    self.logger.debug("Switching to main_menu")
                    self.switch_to("main_menu")

    def update(self):
        return

    def draw(self):
        # 1. Fill background (or blit your JPG here)
        self.screen.fill((30, 30, 30))

        # 2. Render the paragraph (Line by Line)
        for i, line in enumerate(self.text_lines):
            text_surf = self.font.render(line, True, (255, 255, 255))
            # Calculate Y position: Start at 100px, move down 30px per line
            x_pos = (self.screen.get_width() // 2) - (text_surf.get_width() // 2)
            y_pos = 100 + (i * 35)
            self.screen.blit(text_surf, (x_pos, y_pos))

        # 3. Draw the "OK" Button
        pygame.draw.rect(self.screen, (200, 200, 200), self.button_rect, border_radius=5)
        btn_text = self.button_font.render("OK", True, (0, 0, 0))
        text_rect = btn_text.get_rect(center=self.button_rect.center)
        self.screen.blit(btn_text, text_rect)
