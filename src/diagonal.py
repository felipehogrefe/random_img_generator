import random
from src.point_manipulation import PointTool
from PIL import Image

from src.point_manipulation import *

dimensions = (50, 50)
min_rgb = 0
max_rgb = 255

img = Image.new('RGB', dimensions, color=(128,128,128))
img.save('new_img.png')
# img = Image.open('d.png')
# img = img.rotate(90)
pixels = img.load()

step = 50

color_list = []
for x in range(0, 256):
    color_list.append(x)

for x in range(255, 0, -1):
    color_list.append(x)

qtd_colors = len(color_list)

unpainted_points = []
painted_points = []

point_tool = PointTool(dimensions[0], dimensions[1])


def cycle_color(next_color):
    if next_color > qtd_colors:
        print('> qtd_colors', next_color, color_list[next_color - qtd_colors])
        next_color = color_list[next_color - qtd_colors]
    elif next_color < 0:
        print('< 0', next_color, color_list[qtd_colors + next_color])
        next_color = color_list[qtd_colors + next_color]
    return next_color


for x in range(0, dimensions[0]):
    for y in range(0, dimensions[1]):
        unpainted_points.append((x, y))

        r = random.randint(-1*step, step)
        g = random.randint(-1*step, step)
        b = random.randint(-1*step, step)

        if x == 0:
            prev_upper_right = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            prev_upper = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            prev_upper = pixels[x, y-1]
            if x < dimensions[1] - 1:
                prev_upper_right = pixels[x, y-1]
            else:
                prev_upper_right = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if y == 0:
            prev_left = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            prev_left = pixels[x-1, y]
        if x == y and x == 0:
            prev_diagonal = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            prev_diagonal = pixels[x-1, y-1]

        prev_r = (prev_upper[0]+prev_left[0]+prev_diagonal[0])//3
        prev_g = (prev_upper[1]+prev_left[1]+prev_diagonal[1])//3
        prev_b = (prev_upper[2]+prev_left[2]+prev_diagonal[2])//3

        next_r = cycle_color(prev_r + r)
        next_g = cycle_color(prev_g + g)
        next_b = cycle_color(prev_b + b)

        pixels[x, y] = (next_r, next_g, next_b)


img.save('ef.png')
