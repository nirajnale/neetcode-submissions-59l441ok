from collections import defaultdict

class CountSquares:
    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(int))
    
    def add(self, point):
        x, y = point
        self.points[x][y] += 1
    
    def count(self, point):
        qx, qy = point
        total = 0
        
        # use a static list to avoid runtime error
        for x in list(self.points.keys()):
            if x == qx:
                continue
            d = abs(qx - x)
            for y in [qy + d, qy - d]:
                total += self.points[x].get(y, 0) * \
                         self.points[x].get(qy, 0) * \
                         self.points[qx].get(y, 0)
        return total