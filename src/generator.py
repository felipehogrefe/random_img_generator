import random
from PIL import Image

dimensions = (500, 500)
min_rgb = 0
max_rgb = 255

img = Image.new('RGB', dimensions, color='blue')
img.save('new_img.png')
pixels = img.load()

step = 50

for x in range(0, dimensions[0]):
    for y in range(0, dimensions[0]):
        r = random.randrange(-1*step, step)
        g = random.randrange(-1 * step, step)
        b = random.randrange(-1 * step, step)

        if x == 0:
            prev_upper = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        else:
            prev_upper = pixels[x-1, y]
        if y == 0:
            prev_left = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        else:
            prev_left = pixels[x, y-1]
        if x == y and x == 0:
            prev_diagonal = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        else:
            prev_diagonal = pixels[x-1, y-1]

        prev_r = (prev_upper[0]+prev_left[0]+prev_diagonal[0])//3
        prev_g = (prev_upper[1]+prev_left[1]+prev_diagonal[1])//3
        prev_b = (prev_upper[2]+prev_left[2]+prev_diagonal[2])//3

        pixels[x, y] = (prev_r + r, prev_g + g, prev_b + b)

img.save('a.png')
