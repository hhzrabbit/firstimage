import math

def dist(x1, y1, x2, y2):
    return math.sqrt(((x1-x2) ** 2) + ((y1-y2) ** 2))

xres = 500
yres = 500

centerx = 250
centery = 250

pic = open("pic.ppm", "w")

pic.write("P3 %d %d 255\n" % (xres, yres))
for i in range(xres):
    for j in range(yres):
        d = dist(i, j, centerx, centery)
        if d % 10 < 5:
            red = 255
            green = 0
            blue = 0
        else:
            red = 0
            green = 0
            blue = 0
        
        pic.write("%d %d %d\n" % (red, green, blue))

pic.close()

