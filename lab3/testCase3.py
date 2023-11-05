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
# Starting the simulation  
firstWindow = Window(firstSimulation)  
firstWindow.loop()  

