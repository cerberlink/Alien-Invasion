import sys
import pygame as pg
from settings import Settings
from ship import Ship


class AlienInvasion:
    """ Overall class to manage game assets and behavior """

    def __init__(self):
        # Initialize the game, and create game resources
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        # Start the main loop for the game
        while True:
            # watch for keyboard and mouse events
            for event in pg.event.get():
                if event.type == pg.quit:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # make the most recently drawn screen visible
            pg.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    alienInvasion = AlienInvasion()
    alienInvasion.run_game()
