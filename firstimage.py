import math
import random

def dist(x1, y1, x2, y2):
    return math.sqrt(((x1-x2) ** 2) + ((y1-y2) ** 2))

xres = 500
yres = 500


# creates nCircles sets of concentric circles
# each set centered at a random x and a random y
# color of concentric circles greyscaled

# I personally like the way 3 looks
# I'm leaving these here so it's easy to customize
minAmtCircles = 3
maxAmtCircles = 3

nCircles = random.randint(minAmtCircles, maxAmtCircles)
#print nCircles

centers = []
colors = []

for i in range(nCircles):
    centers.append( { 'x': random.randint(0, xres - 1), 'y' : random.randint(0, yres - 1) })
    colors.append( { 'r': random.randint(0, 255), 'g' : random.randint(0, 255), 'b' : random.randint(0, 255) } )

pic = open("pic.ppm", "w")

pic.write("P3 %d %d 255\n" % (xres, yres))
for i in range(xres):
    for j in range(yres):
        red = 0
        green = 0
        blue = 0    
        for index in range(nCircles):
            d = dist(i, j, centers[index]['x'], centers[index]['y']) 
            if d % 10 < 5:
                red = colors[index]['r']
                green = colors[index]['g']
                blue = colors[index]['b']
                break
            
        pic.write("%d %d %d\n" % (red, green, blue))

pic.close()



