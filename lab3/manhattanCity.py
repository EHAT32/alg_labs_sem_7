from trafficFlowSimulator import *
from manhattanGraph import manhattanGraph

# Creating simulation  
manhattanCity = Simulator()  
manhattanCity.createRoadsFromGraph(manhattanGraph)
# manhattanCity.createRoads(roads_vert_down)
# manhattanCity.createRoads(roads_vert_up)  
# manhattanCity.createRoads(roads_hor_right)
# manhattanCity.createRoads(roads_hor_left)

# Starting the simulation  
firstWindow = Window(manhattanCity)  
firstWindow.loop()  