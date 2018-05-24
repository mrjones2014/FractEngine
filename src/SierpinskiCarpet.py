import numpy as numpy
from PIL import Image, ImageOps

n = 6

#make sure the image is a power of 3 relative to the num size
imageSize = 3**n

#Create the image and initialize it as black
image = numpy.empty([imageSize, imageSize, 3], dtype = numpy.uint8)
image.fill(0)

#Any "filled" pixel will be changed to be white
color = numpy.array([255, 255, 255], dtype = numpy.uint8)

for level in range (1, n + 1):
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

#Grab each image that we saved
image_list = ['SierpinskiCarpet1.bmp', 'SierpinskiCarpet2.bmp', 'SierpinskiCarpet3.bmp', 'SierpinskiCarpet4.bmp']

#Open each image so we can modify them
imgs = [Image.open(i) for i in image_list]

#Add a border to each image
imgs = [ImageOps.expand(i, border=20, fill='white') for i in imgs]

#Figure out the minimum shape so we can fit each image to that size
#This shouldn't really matter since they should all be the same size
#but it's a sanity check
min_shape = sorted( [(numpy.sum(i.size), i.size) for i in imgs])[0][1]

#Stack each image horizontally
imgs_comb = numpy.hstack((numpy.asarray(i.resize(min_shape)) for i in imgs))

#Load the image we just made so that we can add an overall border to the 
#whole image
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb_with_border = ImageOps.expand(imgs_comb, border=10, fill='white')

#Finally save the whole thing
imgs_comb_with_border.save("SierpinskiCarpetRow.bmp")
print("Saved File: SierpinskiCarpetRow.bmp")





