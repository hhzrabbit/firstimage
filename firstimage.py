import math

xres = 500
yres = 500

pic = open("pic.ppm", "w")

pic.write("P3 %d %d 255\n" % (xres, yres))
for i in range(xres):
    for j in range(yres):
        iEven = i % 2 == 0
        jEven = j % 2 == 0
        if iEven and jEven:
            red = 255
        else if iEven and  not jEven:
            red = 100
        else if not iEven and jEven:
            red = 255
        else:
            red = 100
        green = 255
        blue = 255     
        pic.write("%d %d %d\n" % (red, green, blue))

pic.close()
