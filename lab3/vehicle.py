import numpy as np

class Vehicle:  
    def __init__(self, config = {}):  
        # Setting default configuration  
        self.set_default_config()  
  
        # Updating the configuration  
        for attr, val in config.items():  
            setattr(self, attr, val)  
  
        # Calculate properties  
        self.initProperties()  
  
    def set_default_config(self):  
        self.l = 2  
        self.s_0 = 2  
        self.T = 1  
        self.vMax = 16.6  
        self.aMax = 2.88  
        self.bMax = 4.61  
  
        self.path = []  
        self.currentRoadIndex = 0  
  
        self.x = 0  
        self.v = self.vMax  
        self.a = 0  
        self.stopped = False  
  
    def initProperties(self):  
        self.sqrt_ab = 2 * np.sqrt(self.aMax * self.bMax)  
        self._vMax = self.vMax  
  
    def update(self, leadVehicle, dt):  
        # Updating the position and velocity  
        if self.v + self.a * dt < 0:  
            self.x -= 1/2 * self.v * self.v / self.a  
            self.v = 0  
        else:  
            self.v += self.a * dt  
            self.x += self.v * dt + self.a * dt * dt/2  
          
        # Updating the acceleration  
        alpha = 0  
        if leadVehicle:  
            del_x = leadVehicle.x - self.x - leadVehicle.l  
            del_v = self.v - leadVehicle.v  
  
            alpha = (self.s_0 + max(0, self.T * self.v + del_v * self.v / self.sqrt_ab)) / del_x  
  
        self.a = self.aMax * (1 - (self.v / self.vMax) ** 4 - alpha ** 2)  
  
        if self.stopped:   
            self.a = - self.bMax * self.v / self.vMax  
          
    def stopVehicle(self):  
        self.stopped = True  
  
    def unstopVehicle(self):  
        self.stopped = False  
  
    def slowVehicle(self, v):  
        self.vMax = v  
  
    def fastVehicle(self):  
        self.vMax = self._vMax  