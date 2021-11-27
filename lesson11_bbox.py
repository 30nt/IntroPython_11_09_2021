def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

class Bbox:
    def __init__(self, x0, y0, x1, y1):  # (x0, y0) left up, (x1, y1) right down
        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1

    def __repr__(self):
        return f"({self._x0}, {self._y0}, {self._x1}, {self._y1})"

    def __add__(self, other):
        x0 = min(self._x0, other._x0)
        y0 = min(self._y0, other._y0)
        x1 = max(self._x1, other._x1)
        y1 = max(self._y1, other._y1)
        return Bbox(x0, y0, x1, y1)

    # @staticmethod
    # def distance(point1, point2):
    #     return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

    def distance(self):
        return ((self._x1 - self._x0) ** 2 + (self._y1 - self._y0) ** 2) ** 0.5


bbox_1 = Bbox(0, 0, 3, 4)
bbox_2 = Bbox(1, 1, 12, 5)
bbox_3 = bbox_1 + bbox_2
print(bbox_3.distance())

print(distance((0, 0), (3, 4)))
