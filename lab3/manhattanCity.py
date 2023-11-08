from trafficFlowSimulator import *
from manhattanGraph import manhattanGraph

# Creating simulation  
manhattanCity = Simulator()  
manhattanCity.createRoadsFromGraph(manhattanGraph)


manhattanCity.createGen({  
    'vehicleRate' : 60,  
    'vehicles' : [  
        [1, {"path" : [(0, 1)]}],  
        [1, {"path" : [(1, 2)]}],  
        [1, {"path" : [(1, 2)]}],  
        [1, {"path" : [(2, 3)]}],  
        [1, {"path" : [(3, 2)]}],
        [1, {"path" : [(4, 1)]}]  
    ]  
})  
trafficRoads = [[manhattanCity.roads[(0, 1)], manhattanCity.roads[(4, 1)]], [manhattanCity.roads[(2, 1)]]]
trafficSignal = TrafficSignal(trafficRoads)
manhattanCity.createTrafficSignals(trafficSignal)


# Starting the simulation  
firstWindow = Window(manhattanCity)  
firstWindow.loop()  