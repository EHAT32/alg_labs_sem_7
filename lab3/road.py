from scipy.spatial import distance
from collections import deque

class Road:
    def __init__(self, start, end, startCross, endCross) -> None:
        self.start = start
        self.end = end
        self.startCross = startCross #idx of a vertex from the graph
        self.endCross = endCross
        self.initProperties()

    def initProperties(self):
        self.length = distance.euclidean(self.start, self.end)
        self.sin = (self.end[1] - self.start[1]) / self.length
        self.cos = (self.end[0] - self.start[0]) / self.length
        self.vehicles = deque()
        self.hasTrafficSignal = False

    def setTrafficSignal(self, signal, group):  
        self.trafficSignal = signal  
        self.trafficSignalGroup = group  
        self.hasTrafficSignal = True  
  
    @property  
    def trafficSignalState(self):  
        if self.hasTrafficSignal:  
            i = self.trafficSignalGroup  
            return self.trafficSignal.currentCycle[i]  
        return True  

    #update vehicles of the road
    def update(self, dt):  
        num = len(self.vehicles)  
          
        if num > 0:  
            # Updating the first vehicle  
            self.vehicles[0].update(None, dt)  
            # Updating the other vehicles  
            for i in range(1, num):  
                lead = self.vehicles[i - 1]  
                self.vehicles[i].update(lead, dt)

            if self.trafficSignalState:  
                # In case the traffic signal is green or does not exist  
                # Then let the vehicles pass  
                self.vehicles[0].unstopVehicle()  
                for the_vehicle in self.vehicles:  
                    the_vehicle.fastVehicle()  
            else:  
                # In case the traffic signal is red  
                if self.vehicles[0].x >= self.length - self.trafficSignal.slowDistance:  
                    # Slowing vehicles down in slowing zone  
                    self.vehicles[0].slowVehicle(self.trafficSignal.slowSpeed)  
                if self.vehicles[0].x >= self.length - self.trafficSignal.stopDistance and self.vehicles[0].x <= self.length - self.trafficSignal.stopDistance / 2:  
                    # Stopping vehicles in the stop zone  
                    self.vehicles[0].stopVehicle()  
    