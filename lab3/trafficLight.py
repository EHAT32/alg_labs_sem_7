class TrafficSignal:  
    def __init__(self, roads, config = {}):  
        # Initializing roads  
        self.roads = roads  
        # Setting the default configuration  
        self.set_default_config()  
        # Updating the configuration  
        for attr, val in config.items():  
            setattr(self, attr, val)  
        # Calculating the properties  
        self.initProperties()  
  
    def set_default_config(self):  
        self.cycle = [(False, True), (True, False)]  
        self.slowDistance = 40  
        self.slowSpeed = 8.3
        self.slowFactor = 10  
        self.stopDistance = 15  
  
        self.currentCycleIndex = 0  
        self.last_t = 0  

    def initProperties(self):  
       for i in range(len(self.roads)):  
           for the_road in self.roads[i]:  
               the_road.setTrafficSignal(self, i)  
  
    @property  
    def currentCycle(self):  
       return self.cycle[self.currentCycleIndex]  
  
    def update(self, simulation):  
       # Going through all cycles every cycleLength and repeats  
       cycleLength = 30  
       m = (simulation.t // cycleLength) % 2  
       self.currentCycleIndex = int(m)   
  