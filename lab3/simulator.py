from road import Road
from copy import deepcopy
from collections import deque
from vehicleGenerator import VehicleGenerators
import numpy as np
from scipy.spatial import distance
import random

class Simulator:
    def __init__(self, config = {}) -> None:
        self.setDefaultConfig()
        #update vals
        for attr, val in config.items():
            setattr(self, attr, val)

    def setDefaultConfig(self):
        #time
        self.t = 520.0
        #time step
        self.dt = 1/60
        #frames count
        self.frameCount = 0
        #roads
        self.roads = {}
        self.vehicleGens = deque()

        self.trafficSignals = deque()

    def createTrafficSignals(self, trafficSignal):
            self.trafficSignals.append(trafficSignal)

    def createRoad(self, start, end, startCross, endCross):
        road = Road(start, end, startCross, endCross)
        self.roads[(startCross, endCross)] = road
        # return road
    
    def createRoads(self, roadsList):
        for roadCoords in roadsList:
            self.createRoad(*roadCoords)

    def createRoadsFromGraph(self, graph):
        self.graph = graph
        for idx in range(len(graph)):
            start = graph[idx][0]
            if len(graph[idx][1]) > 0:
                for vertexIdx in graph[idx][1]:
                    end = (graph[vertexIdx][0][0], graph[vertexIdx][0][1])
                    length = distance.euclidean(start, end)
                    sin = (end[1] - start[1]) / length
                    cos = (end[0] - start[0]) / length
                    self.createRoad((start[0] - 0.3 * sin, start[1] + 0.3 * cos), (end[0] - 0.3 * sin, end[1] + 0.3 * cos), idx, vertexIdx)


    def createGen(self, genConfig):
        self.vehicleGens.append(VehicleGenerators(self, genConfig))

    def update(self):  
        # Updating every road  
        for roadKey in self.roads:
            road = self.roads[roadKey]  
            if len(road.vehicles) > 0 and road.vehicles[0].currentRoadIndex + 1 < len(road.vehicles[0].path):
                vehicle = road.vehicles[0]
                nextRoad = self.roads[vehicle.path[vehicle.currentRoadIndex + 1]]
            else:
                road.update(self.dt)
                nextRoad = None
            road.update(self.dt, nextRoad)  
  
        # Checking the roads for out of bounds vehicle  
        for roadKey in self.roads:  
            road = self.roads[roadKey]
            # If road does not have vehicles, then continue  
            if len(road.vehicles) == 0: continue  
            # If not  
            vehicle = road.vehicles[0]  
            # If the first vehicle is out of road bounds  
            if vehicle.x >= road.length:  
                #if vehicle just wanders:
                if len(vehicle.path) == 1:
                    vehicle.currentRoadIndex = 1
                    newVehicle = deepcopy(vehicle)
                    newVehicle.x = 0
                    crossRoad = self.graph[road.endCross]
                    if len(crossRoad[1]) > 0:
                        if newVehicle.decideToRide():
                            carNums = [len(self.roads[(road.endCross, k)].vehicles) for k in crossRoad[1]]
                            minNum = np.min(carNums)
                            minIdx = [i for i, x in enumerate(carNums) if x == minNum]
                            nextCross = crossRoad[1][random.choice(minIdx)]
                            self.roads[(road.endCross, nextCross)].vehicles.append(newVehicle)
                        else:
                            pass

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

        for signal in self.trafficSignals:  
            signal.update(self)  

        for gen in self.vehicleGens:
            gen.update()
            if (self.t >= 540 and self.t <= 600) or (self.t >= 1020 and self.t <= 1080):
                gen.vehicleRate = 170
            else:
                gen.vehicleRate = 40
        self.t += self.dt

        if self.t >= 1440:
            self.t = 0
