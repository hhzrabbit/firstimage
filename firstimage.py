import math

xres = 500
yres = 500

pic = open("pic.ppm", "w")

pic.write("P3 %d %d 255\n" % (xres, yres))
for i in range(xres):
    for j in range(yres):
        red = 100
        green = 255
        blue = 255     
        pic.write("%d %d %d\n" % (red, green, blue))

pic.close()
