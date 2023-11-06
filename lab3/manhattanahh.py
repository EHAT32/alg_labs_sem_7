roads_vert_down = [((40, 20), (40, 40)),
                   ((40, 40.5), (40, 60)),
                   ((57, 20), (57, 40)),
                   ((57, 40.5), (57, 60))]

roads_vert_up = []

for road in roads_vert_down:
    start_pos = (road[1][0] + 0.5, road[1][1])
    end_pos = (road[0][0] + 0.5, road[0][1])
    roads_vert_up.append((start_pos, end_pos))

roads_hor_right = [((20, 40.5), (40, 40.5)),
                   ((40.5, 40.5), (57, 40.5)),
                   ((57.5, 40.5), (70, 40.5))]

roads_hor_left = []

for road in roads_hor_right:
    start_pos = (road[1][0], road[1][1] - 0.5)
    end_pos = (road[0][0], road[0][1] - 0.5)
    roads_hor_left.append((start_pos, end_pos))