'''
Main.py: The entry point

This module serves as the entry point to the game.
Its purpose is to initialize the game and load data required for operation.
'''

import pygame
import logging
import sys
import os
from pathlib import Path

from dotenv import load_dotenv

def _load_env_file():
    config_dir = Path(__file__).parent.parent / "config"
    env_name = os.environ.get(".env").lower()
    env_file = config_dir / ".env"

    load_dotenv(env_file)

    # Set up global logging level from LOG_LEVEL env var
    log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
    numeric_level = getattr(logging, log_level, logging.INFO)
    logging.basicConfig(level=numeric_level, format='[$(levelname)s] $(message)s')
    logging.info("Logging initialized at level %s, if you didn't request this check the LOG_LEVEL variable in your .env file.", log_level)
    logging.info("[env] Loaded environment file: %s", env_file)


def get_screen(width, height):
    pygame.display.set_caption()
    return pygame.display.set_mode((width, height))

def run_game_loop(screen):
    '''The infinite loop that is the game running.'''
    game_playing = True

    while game_playing:
        game_playing = False

    return


def main():
    '''The main entry point of our game.'''

    # Load ENV 
    _load_env_file()

    # Initialize Pygame
    pygame.init()
    
    screen = get_screen()
    # Run Game Loop
    run_game_loop(screen)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()