import numpy as numpy
from PIL import Image

n = 6

#make sure the image is a power of 3 relative to the num size
imageSize = 3**n

#Create the image and initialize it as black
image = numpy.empty([imageSize, imageSize, 3], dtype = numpy.uint8)
image.fill(0)

#Any "filled" pixel will be changed to be white
color = numpy.array([255, 255, 255], dtype = numpy.uint8)

for level in range (0, n + 1):
    stepSize = 3**(n - level)
    for x in range(0, 3**level):
        if x % 3 == 1:
            for y in range (0, 3**level):
                if y % 3 == 1:
                    #if we get here, the pixel is "filled", so set the color to white
                    image[y * stepSize : (y+1) * stepSize, x * stepSize : (x + 1) * stepSize] = color

    #Send to image and save the file
    outputFilename = "SierpinskiCarpet%d.bmp" % level
    Image.fromarray(image).save("SierpinskiCarpet%d.bmp" % level)
    print("Saved Filed: %s" % outputFilename)

image_list = ['SierpinskiCarpet1.bmp', 'SierpinskiCarpet2.bmp', 'SierpinskiCarpet3.bmp', 'SierpinskiCarpet4.bmp']
imgs = [Image.open(i) for i in image_list]

min_shape = sorted( [(numpy.sum(i.size), i.size) for i in imgs])[0][1]
imgs_comb = numpy.hstack((numpy.asarray(i.resize(min_shape)) for i in imgs))

imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save("test.bmp")




