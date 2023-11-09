import numpy as np
from scipy.spatial import distance

togliattiGraph = np.array([[(40, 20), (1, 3)],
                           [(60, 20), (0, 2, 4)],
                           [(60, 40), (1, 3, 5, 6)],
                           [(40, 40), (0, 2, 7)],
                           [(80, 20), (1, 5)],
                           [(80, 40), (2, 4)],
                           [(60, 60), (2, )],
                           [(20, 40), (3, )]], dtype = object)

# def createRoadsFromGraph(graph):
#     roads = []

#     for vertex in graph:
#         start = (vertex[0][0], vertex[0][1])
#         if len(vertex[1]) > 0:
#             for vertexIdx in vertex[1]:
#                 end = (graph[vertexIdx][0][0], graph[vertexIdx][0][1])
#                 length = distance.euclidean(start, end)
#                 sin = (end[1] - start[1]) / length
#                 cos = (end[0] - start[0]) / length
#                 roads.append(((start[0] + 0.3 * sin, start[1] + 0.3 * cos), (end[0] + 0.3 * sin, end[1] + 0.3 * cos)))

#     return roads

# manhRoads = createRoadsFromGraph(togliattiGraph)