from road import Road

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
        self.roads = []

    def createRoad(self, start, end):
        road = Road(start, end)
        self.roads.append(road)
        return road
    
    def createMultipleRoads(self, roadsList):
        for road in roadsList:
            self.createRoad(*road)