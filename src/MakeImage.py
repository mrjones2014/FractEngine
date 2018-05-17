from PIL import Image


def from_pixel_colors(pixels):
    width = len(pixels)
    height = len(pixels[0])
    picture = Image.new("RGB", (width, height))
    for x in range(len(pixels)):
        for y in range(len(pixels[x])):
            picture.putpixel((x, y), pixels[x][y])
    return picture