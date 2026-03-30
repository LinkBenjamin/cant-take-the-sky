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
from app.screens.main_menu import MainMenu
from app.screens.scene_manager import SceneManager

def _setup_logging():
    '''Set up global logging level from LOG_LEVEL env var'''
    log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
    numeric_level = getattr(logging, log_level, logging.INFO)
    logging.basicConfig(level=numeric_level, format='[%(levelname)s] %(message)s')
    logging.info("Logging initialized at level %s, if you didn't request this check the LOG_LEVEL variable in your .env file.", log_level)

def _load_env_file():
    '''Load the .env file'''
    config_dir = Path(__file__).parent.parent.parent / "config"
    env_file = config_dir / ".env"
    print(f"[DEBUG] Looking for env at {env_file.absolute()}")
    if not env_file.exists():
        print("[ERROR] .env file not found at that location!")
    success = load_dotenv(env_file)
    print(f"[DEBUG] Load successful? {success}")

def get_screen(width, height):
    '''Get the pygame screen object'''
    gamename = os.environ.get("GAME_NAME")
    pygame.display.set_caption(gamename if gamename else "ERROR LOADING GAME_NAME FROM .env")
    return pygame.display.set_mode((width, height))

def main():
    '''The main entry point of our game.'''

    # Load ENV 
    _load_env_file()

    # Set up logging
    _setup_logging()

    # Initialize Pygame
    pygame.init()

    logging.debug("Pygame initialized, screen object created. Starting game loop...")

    # Hand control to the Manager
    manager = SceneManager()
    
    # Start the infinite loop inside the manager
    manager.run()

    # 5. Clean exit
    pygame.quit()

    logging.debug("Quit request detected, shutting down...")
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()