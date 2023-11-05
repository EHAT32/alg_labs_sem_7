from road import Road
from copy import deepcopy
from collections import deque
from vehicleGenerator import VehicleGenerators

class Simulator:
    def __init__(self, config = {}) -> None:
        self.setDefaultConfig()

        #update vals
        for attr, val in config.items():
            setattr(self, attr, val)

    def setDefaultConfig(self):
        #time
        self.t = .0
        #time step
        self.dt = 1/60
        #frames count
        self.frameCount = 0
        #roads
        self.roads = deque()

        self.vehicleGens = deque()

    def createRoad(self, start, end):
        road = Road(start, end)
        self.roads.append(road)
        return road
    
    def createRoads(self, roadsList):
        for roadCoords in roadsList:
            self.createRoad(*roadCoords)

    def createGen(self, genConfig):
        self.vehicleGens.append(VehicleGenerators(self, genConfig))

    def update(self):  
        # Updating every road  
        for road in self.roads:  
            road.update(self.dt)  
  
        # Checking the roads for out of bounds vehicle  
        for road in self.roads:  
            # If road does not have vehicles, then continue  
            if len(road.vehicles) == 0: continue  
            # If not  
            vehicle = road.vehicles[0]  
            # If the first vehicle is out of road bounds  
            if vehicle.x >= road.length:  
                # If vehicle has a next road  
                if vehicle.currentRoadIndex + 1 < len(vehicle.path):  
                    # Updating the current road to next road  
                    vehicle.currentRoadIndex += 1  
                    # Creating a copy and reseting some vehicle properties  
                    newVehicle = deepcopy(vehicle)  
                    newVehicle.x = 0  
                    # Adding it to the next road  
                    nextRoadIndex = vehicle.path[vehicle.currentRoadIndex]  
                    self.roads[nextRoadIndex].vehicles.append(newVehicle)  
                # In all cases, removing it from its road  
                road.vehicles.popleft()  

        self.t += self.dt

        for gen in self.vehicleGens:
            gen.update()

