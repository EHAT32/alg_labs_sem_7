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
  
    def run(self, stepsPerUpdate = 1):  
        """Running the simulation by updating in every loop."""  
        def loop(sim):  
            sim.run(stepsPerUpdate)  
        self.loop(loop)  
  
    def loop(self, loop = None):  
        """Showing a window visualizing the simulation and runs the loop function."""  
        # Creating a pygame window  
        self.screen = pygame.display.set_mode((self.the_width, self.the_height), pygame.WINDOWMAXIMIZED)  
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
            
            self.simulate.update()
  
            # Drawing simulation  
            self.draw()  
  
            # Updating the window  
            pygame.display.update()  
            clock.tick(self.the_fps)  
  
            # Handling all events  
            for event in pygame.event.get():  
                ...
  
    def convert(self, x, y):  
        """Converting the simulation coordinates to screen coordinates"""  
        #the goal is to convert max 160 x 90 coords into 1920 x 1080
        height = 1080
        width = 1920
        max_x = 160
        max_y = 90
        screen_x = width * x / max_x
        screen_y = height * y / max_y
        return screen_x, screen_y
  
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
  
    def the_circle(self, pos, radius = 3, color = (0,0,255), filled = True):  
        pygame.draw.circle(self.screen, color, pos, radius)
  
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
            start = self.convert(*road.start)
            end = self.convert(*road.end)
            self.the_line(start, end, color) 
  
    def drawVehicles(self):
        for road in self.simulate.roads:
            if len(road.vehicles) >= 1:
                for car in road.vehicles:
                    positionX, positionY = road.start
                    positionX += car.x * road.cos
                    positionY += car.x * road.sin
                    position = self.convert(positionX, positionY)
                    self.the_circle(position)
  
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
  
        self.drawVehicles()
        # Drawing the status info  
        self.drawStatus()  