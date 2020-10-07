import random
from PIL import Image

dimensions = (500, 500)
min_rgb = 0
max_rgb = 255

img = Image.new('RGB', dimensions, color=(127, 127, 127))
img.save('new_img.png')
pixels = img.load()

step = 5

for x in range(0, dimensions[0]):
    for y in range (0, dimensions[0]):
        r = random.randrange(-1*step, step)
        g = random.randrange(-1 * step, step)
        b = random.randrange(-1 * step, step)
        print(r,g,b)
        prev_pixel = pixels[x-1 if x !=0 else x,y-1 if y!=0 else y]

        pixels[x,y] = (prev_pixel[0] + r, prev_pixel[1]+g, prev_pixel[2]+b)

img.save('a.png')
