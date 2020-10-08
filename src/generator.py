import random
from src.point_manipulation import PointTool
from PIL import Image

from src.point_manipulation import *

dimensions = (500, 500)
min_rgb = 0
max_rgb = 255

img = Image.new('RGB', dimensions, color='white')
img.save('new_img.png')
# img = Image.open('d.png')
# img = img.rotate(90)
pixels = img.load()

step = 50

unpainted_points = []
painted_points = []

point_tool = PointTool(dimensions[0], dimensions[1])

for x in range(0, dimensions[0]):
    for y in range(0, dimensions[1]):
        unpainted_points.append((x,y))

        r = random.randrange(-1 * step, step)
        g = random.randrange(-1 * step, step)
        b = random.randrange(-1 * step, step)

        if x == 0:
            prev_upper_right = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
            prev_upper = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        else:
            prev_upper = pixels[x, y-1]
            if x < dimensions[1] -1:
                prev_upper_right = pixels[x, y-1]
            else:
                prev_upper_right = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

        if y == 0:
            prev_left = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        else:
            prev_left = pixels[x-1, y]
        if x == y and x == 0:
            prev_diagonal = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        else:
            prev_diagonal = pixels[x-1, y-1]

        prev_r = (prev_upper[0]+prev_left[0]+prev_diagonal[0]+prev_upper_right[0])//4
        prev_g = (prev_upper[1]+prev_left[1]+prev_diagonal[1]+prev_upper_right[1])//4
        prev_b = (prev_upper[2]+prev_left[2]+prev_diagonal[2]+prev_upper_right[2])//4

        pixels[x, y] = (prev_r + r, prev_g + g, prev_b + b)


img.save('e.png')


def find_surronding_empty(coordinate):
    pass


def northwest_point(point):
    return point[0] - 1, point[1] - 1


def north_point(point):
    return point[0], point[1] + 1


def northeast_point(point):
    return point[0] + 1, point[1] - 1


def west_point(point):
    return point[0] - 1, point[1]


def east_point(point):
    return point[0] + 1, point[1]


def southwest_point(point):
    return point[0] - 1, point[1] + 1


def south_point(point):
    return point[0], point[1] + 1


def southeast_point(point):
    return point[0] + 1, point[1] + 1
