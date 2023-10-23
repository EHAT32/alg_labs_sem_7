from scipy.spatial import distance

class Road:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def initProperties(self):
        self.length = distance.euclidean(self.start, self.end)
        self.sin = (self.end[1] - self.start[1]) / self.length
        self.cos = (self.end[0] - self.start[0]) / self.length
    