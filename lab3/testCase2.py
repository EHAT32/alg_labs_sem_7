from trafficFlowSimulator import *

# Creating simulation  
firstSimulation = Simulator()  
  
# Adding one road  
# firstSimulation.createRoad((0, 0), (1920, 1080)) 
# firstSimulation.createRoad((0,0), (1000, 800)) 
  
# Adding multiple roads  
# firstSimulation.createRoads([  
#     ((10, 45), (150, 45)),
#     ((150, 45.5), (10, 45.5)),
#     ((75,20), (75, 60)),
#     ((75.5,60), (75.5, 20))
      
# ])  
firstSimulation.createRoads(roads)
firstSimulation.roads[0].vehicles.append(  
    Vehicle({  
        "path" : [0, 1, 2, 3]  
    })  
)  
  
firstSimulation.roads[0].vehicles.append(Vehicle())  
firstSimulation.roads[1].vehicles.append(Vehicle())  
firstSimulation.roads[2].vehicles.append(Vehicle())  
firstSimulation.roads[3].vehicles.append(Vehicle())  

# Starting the simulation  
firstWindow = Window(firstSimulation)  
firstWindow.loop()  

