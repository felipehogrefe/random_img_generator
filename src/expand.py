import random
from src.point_manipulation import PointTool
from PIL import Image

from src.point_manipulation import *

dimensions = (500, 500)
min_rgb = 0
max_rgb = 255

# img = Image.new('RGB', dimensions, color=(128,128,128))
# img.save('new_img.png')
img_old = Image.open('new_img2.png')
pixels_old = img_old.load()

width, height = img_old.size
img = Image.new('RGB', (width*2, height*2), color='black')
img.save('new_img3.png')
pixels = img.load()

empty = []
for x in range(0, width*2):
    for y in range(0, height*2):
        empty.append((x, y))

for x in range(0, width):
    for y in range(0, height):
        pixels[x*2, y*2] = pixels_old[x, y]
        empty.remove((x*2, y*2))

point_tool = PointTool(width*2, height*2)

for pi in empty:

    if pi[0] % 2 == 0 or pi[0] == 0:
        north_point = point_tool.north_point(pi)
        south_point = point_tool.south_point(pi)
        total = (1 if north_point else 0) + (1 if south_point else 0)
        pixels[pi] = (
            ((pixels[north_point][0] if north_point != 0 else 0) + (pixels[south_point][0] if south_point != 0 else 0)) // total,
            ((pixels[north_point][1] if north_point != 0 else 0) + (pixels[south_point][1] if south_point != 0 else 0)) // total,
            ((pixels[north_point][2] if north_point != 0 else 0) + (pixels[south_point][2] if south_point != 0 else 0)) // total,
        )
        if not south_point:
            print(pi, pixels[pi], pixels[north_point])

    elif pi[1] % 2 == 0:
        west_point = point_tool.west_point(pi)
        east_point = point_tool.east_point(pi)
        total = (1 if west_point else 0) + (1 if east_point else 0)
        pixels[pi] = (
            ((pixels[west_point][0] if west_point != 0 else 0) + (pixels[east_point][0] if east_point != 0 else 0)) // total,
            ((pixels[west_point][1] if west_point != 0 else 0) + (pixels[east_point][1] if east_point != 0 else 0)) // total,
            ((pixels[west_point][2] if west_point != 0 else 0) + (pixels[east_point][2] if east_point != 0 else 0)) // total,
        )

    else:

        northeast_point = point_tool.northeast_point(pi)
        southeast_point = point_tool.southeast_point(pi)
        northwest_point = point_tool.northwest_point(pi)
        southwest_point = point_tool.southwest_point(pi)
        total = (1 if northeast_point else 0) + (1 if southeast_point else 0) + (1 if northwest_point else 0) + (1 if southwest_point else 0)
        pixels[pi] = (
            ((pixels[northeast_point][0] if northeast_point != 0 else 0) + (pixels[southeast_point][0] if southeast_point != 0 else 0) +
             (pixels[northwest_point][0] if northwest_point != 0 else 0) + (pixels[southwest_point][0] if southwest_point != 0 else 0)) // total,

            ((pixels[northeast_point][1] if northeast_point != 0 else 0) + (pixels[southeast_point][1] if southeast_point != 0 else 0) +
             (pixels[northwest_point][1] if northwest_point != 0 else 0) + (pixels[southwest_point][1] if southwest_point != 0 else 0)) // total,

            ((pixels[northeast_point][2] if northeast_point != 0 else 0) + (pixels[southeast_point][2] if southeast_point != 0 else 0) +
             (pixels[northwest_point][2] if northwest_point != 0 else 0) + (pixels[southwest_point][2] if southwest_point != 0 else 0)) // total,
        )

img.save('new_img3.png')
