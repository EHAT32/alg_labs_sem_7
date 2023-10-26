from trafficFlowSimulator import *

# Creating simulation  
firstSimulation = Simulator()  
  
# Adding one road  
# firstSimulation.createRoad((0, 0), (1920, 1080)) 
# firstSimulation.createRoad((0,0), (1000, 800)) 
  
# Adding multiple roads  
firstSimulation.createRoads([  
    ((10, 45), (150, 45)),
    ((150, 45.5), (10, 45.5)),
    ((75,20), (75, 60)),
    ((75.5,60), (75.5, 20))
      
])  
# Starting the simulation  
firstWindow = Window(firstSimulation)  
firstWindow.loop()  