from trafficFlowSimulator import *
from togliattiGraph import togliattiGraph

# Creating simulation  
togliattiCity = Simulator()  
togliattiCity.createRoadsFromGraph(togliattiGraph)


togliattiCity.createGen({  
    'vehicleRate' : 40,  
    'vehicles' : [  
        [1, {"path" : [(0, 1), (1, 2), (2, 5)]}],  
        [1, {"path" : [(7, 3), (3, 2), (2, 1), (1, 4)]}],  
        [1, {"path" : [(4, 1), (1, 2), (2, 6)]}],  
        [1, {"path" : [(6, 2), (2, 5)]}],  
        [1, {"path" : [(6, 2), (2, 3), (3, 0)]}],
        [1, {"path" : [(7, 3), (3, 2), (2, 5)]}]  
    ]  
})  
trafficRoads1 = [[togliattiCity.roads[(0, 1)], togliattiCity.roads[(4, 1)]], [togliattiCity.roads[(2, 1)]]]
trafficRoads2 = [[togliattiCity.roads[(1, 2)], togliattiCity.roads[(6, 2)]], [togliattiCity.roads[(3, 2)], togliattiCity.roads[(5, 2)]]]
trafficRoads3 = [[togliattiCity.roads[(7, 3)], togliattiCity.roads[(2, 3)]], [togliattiCity.roads[(0, 3)], ]]
trafficSignal1 = TrafficSignal(trafficRoads1)
trafficSignal2 = TrafficSignal(trafficRoads2)
trafficSignal3 = TrafficSignal(trafficRoads3)
togliattiCity.createTrafficSignals(trafficSignal1)
togliattiCity.createTrafficSignals(trafficSignal2)
togliattiCity.createTrafficSignals(trafficSignal3)

# Starting the simulation  
firstWindow = Window(togliattiCity)  
firstWindow.loop()  