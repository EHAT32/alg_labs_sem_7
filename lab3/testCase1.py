from trafficFlowSimulator import *

# Creating simulation  
firstSimulation = Simulator()  
  
# Adding one road  
# firstSimulation.createRoad((0, 0), (1920, 1080)) 
# firstSimulation.createRoad((0,0), (1000, 800)) 
  
# Adding multiple roads  
firstSimulation.createRoads([  
    ((0, 1000), (0, 1000)),  
    ((0, 1200), (300, 1000)),  
    ((180, 61), (0, 61)),  
    ((220, 56), (180, 61)),  
    ((300, 31), (220, 56)),  
    ((180, 61), (160, 97)),  
    ((158, 131), (300, 131)),  
    ((0, 179), (300, 179)),  
    ((300, 181), (0, 181)),  
    ((160, 101), (156, 180))  
      
])  
print(firstSimulation.roads) 
# Starting the simulation  
firstWindow = Window(firstSimulation)  
firstWindow.loop()  