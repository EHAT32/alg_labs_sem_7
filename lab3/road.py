from scipy.spatial import distance
from collections import deque

class Road:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def initProperties(self):
        self.length = distance.euclidean(self.start, self.end)
        self.sin = (self.end[1] - self.start[1]) / self.length
        self.cos = (self.end[0] - self.start[0]) / self.length
        self.vehicles = []

    def update(self, dt):  
        num = len(self.vehicles)  
          
        if num > 0:  
            # Updating the first vehicle  
            self.vehicles[0].update(None, dt)  
            # Updating the other vehicles  
            for i in range(1, num):  
                lead = self.vehicles[i - 1]  
                self.vehicles[i].update(lead, dt)
    