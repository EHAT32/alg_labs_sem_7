import pygame
from pygame import gfxdraw
import numpy as np

class Window:  
    def __init__(self, simulate, config = {}):  
        # Simulation to draw  
        self.simulate = simulate  
  
        # Setting the default configurations  
        self.set_default_config()  
  
        # Updating the configurations  
        for attr, val in config.items():  
            setattr(self, attr, val)  
          
    def set_default_config(self):  
        """Setting the default configuration"""  
        self.the_width = 1920  
        self.the_height = 1080  
        self.the_bgColor = (250, 250, 250)  
  
        self.the_fps = 60  
        self.the_zoom = 5  
        self.the_offset = (0, 0)  
  
        self.mouseLast = (0, 0)  
        self.mouseDown = False  
  
    def loop(self, loop = None):  
        """Showing a window visualizing the simulation and runs the loop function."""  
        # Creating a pygame window  
        self.screen = pygame.display.set_mode((self.the_width, self.the_height), pygame.FULLSCREEN)  
        pygame.display.flip()  
  
        # Fixed fps  
        clock = pygame.time.Clock()  
  
        # To draw text  
        pygame.font.init()  
        self.text_font = pygame.font.SysFont('Lucida Console', 16)  
  
        # Drawing loop  
        running = True  
        while running:  
            # Updating the simulation  
            if loop: loop(self.simulate)  
  
            # Drawing simulation  
            self.draw()  
  
            # Updating the window  
            pygame.display.update()  
            clock.tick(self.the_fps)  
  
            # Handling all events  
            for event in pygame.event.get():  
                # Handling mouse drag and wheel events  
                ...  
  
    def convert(self, x, y = None):  
        """Converting the simulation coordinates to screen coordinates"""  
        ...  
  
    def inverseConvert(self, x, y = None):  
        """Converting the screen coordinates to simulation coordinates"""  
        ...  
  
    def the_background(self, r, g, b):  
        self.screen.fill(self.the_bgColor)
          
    def the_line(self, start_pos, end_pos, color):  
        pygame.draw.line(self.screen, color, start_pos, end_pos, 5)
  
    def the_rect(self, pos, size, color):  
        """Drawing a rectangle."""  
        ...  
  
    def the_box(self, pos, size, color):  
        """Drawing a rectangle."""  
        ...  
  
    def the_circle(self, pos, radius, color, filled = True):  
        """Drawing a circle"""  
        ...  
  
    def the_polygon(self, vertices, color, filled = True):  
        """Drawing a polygon"""  
  
    def the_rotated_box(self, pos, size, angle = None, cos = None, sin = None, centered = True, color = (0, 0, 255), filled = True):  
        """Drawing a filled rectangle centered at *pos* with size *size* rotated anti-clockwise by *angle*."""  
  
    def the_rotated_rect(self, pos, size, angle = None, cos = None, sin = None, centered = True, color = (0, 0, 255)):  
        """Drawing a rectangle centered at *pos* with size *size* rotated anti-clockwise by *angle*."""  
  
    def drawAxes(self, color = (100, 100, 100)):  
        """Drawing x and y axis"""  
  
    def drawGrid(self, unit = 50, color = (150, 150, 150)):  
        """Drawing a grid"""  
  
    def drawRoads(self, color=(128,128,128)):  
        for road in self.simulate.roads:
            self.the_line(road.start, road.end, color) 
  
    def drawStatus(self):  
        """Drawing status text"""  
  
    def draw(self):  
        # Filling the background  
        self.the_background(*self.the_bgColor)  
  
        # Major and minor grid and axes  
        self.drawGrid(10, (220, 220, 220))  
        self.drawGrid(100, (200, 200, 200))  
        self.drawAxes()  
  
        # Drawing roads  
        self.drawRoads()  
  
        # Drawing the status info  
        self.drawStatus()  