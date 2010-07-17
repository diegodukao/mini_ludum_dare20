#! /usr/bin/env python

import sys
import pygame
from helpers import *

class GameMain:
    """The Main Game Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, width=800, height=600):
        """Initialize PyGame"""
        pygame.init
        
        """Set the window size"""
        self.width = width
        self.height = height
        
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        """Create the background"""
        self.bg, self.bg_rect = load_image("ocean.jpg")
        self.bg = self.bg.convert()

    
    def MainLoop(self):
        """This is the Main Loop of the game"""
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.blit(self.bg, self.bg_rect)
            pygame.display.flip()


if __name__ == "__main__":
    MainWindow = GameMain()
    MainWindow.MainLoop()

