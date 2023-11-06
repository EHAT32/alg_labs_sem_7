from trafficFlowSimulator import *

# Creating simulation  
firstSimulation = Simulator()  
  
firstSimulation.createRoads(roads) 
  
firstSimulation.createGen({  
    'vehicleRate' : 60,  
    'vehicles' : [  
        [1, {"path" : [3, 2, 1]}],  
        [1, {"path" : [4]}],  
        [1, {"path" : [4]}],  
        [1, {"path" : [4]}],  
        [1, {"path" : [4]}]  
    ]  
})  
roads = firstSimulation.roads
trafficRoads = [[roads[0], roads[2]], [roads[1], roads[3]]]
trafficSignal = TrafficSignal(trafficRoads)
firstSimulation.createTrafficSignals(trafficSignal)

# Starting the simulation  
firstWindow = Window(firstSimulation)  
firstWindow.loop()  

