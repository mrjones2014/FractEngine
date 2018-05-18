import numpy as numpy
from PIL import Image

numLevels = 6

#make sure the image is a power of 3 relative to the num size
imageSize = 3**numLevels

#Create the image and initialize it as black
image = numpy.empty([imageSize, imageSize, 3], dtype = numpy.uint8)
image.fill(0)

#Any "filled" pixel will be changed to be white
color = numpy.array([255, 255, 255], dtype = numpy.uint8)

for level in range (0, numLevels + 1):
    stepSize = 3**(numLevels - level)
    for x in range(0, 3**level):
        if x % 3 == 1:
            for y in range (0, 3**level):
                if y % 3 == 1:
                    #if we get here, the pixel is "filled", so set the color to white
                    image[y * stepSize : (y+1) * stepSize, x * stepSize : (x + 1) * stepSize] = color

    #Send to image and save the file
    #outputFilename = "SierpinskiCarpet%d.bmp" % level
    Image.fromarray(image).show("SierpinskiCarpet%d" % level)
    if (level != numLevels):
        input("Press Escape to close image and enter to get the next...")
    else:
        input("Press Escape and then enter to close the program")
    #print("Saved Filed: %s" % outputFilename)