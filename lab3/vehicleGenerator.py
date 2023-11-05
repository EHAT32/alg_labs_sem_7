from numpy.random import randint
from vehicle import Vehicle

class VehicleGenerators:  
    def __init__(self, sim, config = {}):  
        self.set_default_config()
        self.simulation = sim
        self.lastAddedTime = self.simulation.t
        for attr, val in config.items():
            setattr(self, attr, val)
        self.initProperties()
  
    def set_default_config(self):  
        self.vehicleRate = 20  
        self.vehicles = [  
            (1, {})  
        ]  
  
    def initProperties(self):  
        self.upcomingVehicle = self.generateVehicle()  
  
    def generateVehicle(self):  
        """Returning a random vehicle from self.vehicles with random proportions"""  
        total = sum(pair[0] for pair in self.vehicles)  
        n = randint(1, total + 1)  
        for (weight, config) in self.vehicles:  
            n -= weight  
            if n <= 0:  
                return Vehicle(config)  
  
    def update(self):  
        """Adding vehicles"""  
        if abs(self.simulation.t - self.lastAddedTime) >= 60 / self.vehicleRate:  
            # If time elapsed after the last added vehicle is  
            # greater than vehicle period; then generate a vehicle  
            road = self.simulation.roads[self.upcomingVehicle.path[0]]        
            if len(road.vehicles) == 0 or road.vehicles[-1].x > self.upcomingVehicle.s_0 + self.upcomingVehicle.l:  
                # If there is space for the generated vehicle; then add it  
                self.upcomingVehicle.timeAdded = self.simulation.t  
                road.vehicles.append(self.upcomingVehicle)  
                # Resetting lastAddedTime and upcomingVehicle  
                self.lastAddedTime = self.simulation.t  
            self.upcomingVehicle = self.generateVehicle()  