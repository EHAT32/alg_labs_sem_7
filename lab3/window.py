import pygame
from pygame import gfxdraw
import numpy as np

class Window:
    def __init__(self, simulate, config = {}) -> None:
        self.simulate = simulate
        self.setDefaultConfig()

    def set_default_config(self):  
        """Setting the default configuration"""  
        self.width = 1400  
        self.height = 1000  
        self.bgColor = (250, 250, 250)  
  
        self.fps = 60  
        self.zoom = 5  
        self.offset = (0, 0)  
  
        self.mouseLast = (0, 0)  
        self.mouseDown = False  