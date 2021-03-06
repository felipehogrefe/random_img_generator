NORTH_BOUNDARY = 1
EAST_BOUNDARY = 2
SOUTH_BOUNDARY = 3
WEST_BOUNDARY = 4
NORTHEAST_BOUNDARY = 5
NORTHWEST_BOUNDARY = 6
SOUTHEAST_BOUNDARY = 7
SOUTHWEST_BOUNDARY = 8


class PointTool:

    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y

    def check_boundary(self, point):
        if point[0] == 0:
            if point[1] == 0:
                return NORTHWEST_BOUNDARY
            if point[1] == self.max_y:
                return SOUTHWEST_BOUNDARY
            else:
                return WEST_BOUNDARY
        if point[0] == self.max_x:
            if point[1] == 0:
                return NORTHEAST_BOUNDARY
            if point[1] == self.max_y:
                return SOUTHEAST_BOUNDARY
            else:
                return EAST_BOUNDARY

        if point[1] == 0:
            return NORTH_BOUNDARY
        if point[1] == self.max_y:
            return SOUTH_BOUNDARY
        return 0

    def northwest_point(self, point):
        if point[0] - 1 >= 0 and point[1] - 1 >= 0:
            return point[0] - 1, point[1] - 1
        return 0

    def north_point(self, point):
        if point[1] - 1 >= 0:
            return point[0], point[1] - 1
        return 0

    def northeast_point(self, point):
        if point[0] + 1 < self.max_x and point[1] - 1 >= 0:
            return point[0] + 1, point[1] - 1
        return 0

    def west_point(self, point):
        if point[0] - 1 >= 0:
            return point[0] - 1, point[1]
        return 0

    def east_point(self, point):
        if point[0] + 1 < self.max_x:
            return point[0] + 1, point[1]
        return 0

    def southwest_point(self, point):
        if point[0] - 1 >= 0 and point[1] + 1 < self.max_y:
            return point[0] - 1, point[1] + 1
        return 0

    def south_point(self, point):
        if point[1] + 1 < self.max_y:
            return point[0], point[1] + 1
        return 0

    def southeast_point(self, point):
        if point[0] + 1 < self.max_x and point[1] + 1 < self.max_y:
            return point[0] + 1, point[1] + 1
        return 0
