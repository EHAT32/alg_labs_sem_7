from trafficFlowSimulator import *
from manhattanGraph import manhattanGraph

# Creating simulation  
manhattanCity = Simulator()  
manhattanCity.createRoadsFromGraph(manhattanGraph)
# manhattanCity.createRoads(roads_vert_down)
# manhattanCity.createRoads(roads_vert_up)  
# manhattanCity.createRoads(roads_hor_right)
# manhattanCity.createRoads(roads_hor_left)

manhattanCity.createGen({  
    'vehicleRate' : 60,  
    'vehicles' : [  
        [1, {"path" : [(0, 1)]}],  
        [1, {"path" : [(1, 2)]}],  
        [1, {"path" : [(1, 2)]}],  
        [1, {"path" : [(2, 3)]}],  
        [1, {"path" : [(3, 2)]}]  
    ]  
})  

# Starting the simulation  
firstWindow = Window(manhattanCity)  
firstWindow.loop()  