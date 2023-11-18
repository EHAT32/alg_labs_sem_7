from scipy.spatial import distance
from collections import deque

class CapacityTracker:
    def __init__(self):
        self.capacity = 0
        self.startTime = None
        self.duration = 0

    def updateCapacity(self, newCapacity, currentTime):
        if newCapacity >= 90 and self.capacity < 90:  # Capacity just crossed 90
            self.startTime = currentTime
        elif newCapacity < 90 and self.capacity >= 90:  # Capacity just dropped below 90
            if self.startTime is not None:
                self.duration = currentTime - self.startTime
                self.startTime = None
        elif newCapacity < 90:
            self.duration = 0
        self.capacity = newCapacity

    def getDurationOver90(self, currentTime):
        if self.startTime is not None:  # If capacity is currently over 90
            return self.duration + (currentTime - self.startTime)
        else:
            return self.duration
class Road:
    def __init__(self, start, end, startCross, endCross) -> None:
        self.start = start
        self.end = end
        self.startCross = startCross #idx of a vertex from the graph
        self.endCross = endCross
        self.initProperties()
        self.capacityTracker = CapacityTracker()

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
    def update(self, dt, currentTime, nextRoad = None, nextRoadAmount = 12):  
        num = len(self.vehicles)  
        carLen = 1.5
        capacity = carLen * num / self.length * 100
        self.capacityTracker.updateCapacity(capacity, currentTime)
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
                if nextRoad is not None:
                    if len(nextRoad.vehicles) >= nextRoadAmount and self.vehicles[0].x >= self.length - self.trafficSignal.stopDistance * 0.6:
                        self.vehicles[0].v = 0
                        self.vehicles[0].stopVehicle()
                        # for the_vehicle in self.vehicles:
                        #     the_vehicle.slowVehicle(self.trafficSignal.slowSpeed)
                    else:
                        self.vehicles[0].unstopVehicle()  
                        for the_vehicle in self.vehicles:  
                            the_vehicle.fastVehicle()
                else:
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
    