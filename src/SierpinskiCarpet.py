from decimal import Decimal
import MakeImage
import math

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

def make_matrix(w, h):
    return [[0 for x in range(w)] for y in range(h)]

def put_pixels(image, pixels, height, width):
    for x in range(width):
        for y in range(height):
            image.putpixel((x, y), pixels[x][y])

class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.filled = 0
    
    def filled_check(self, n):
        if n >= 1:
            if (self.x % 3 == 2 and self.y % 3 == 2):
                self.filled = 1
            else:
                self.x = math.ceil(self.x / 3)
                self.y = math.ceil(self.y / 3)
                self.filled_check(n - 1)
        
class SierpinskiCarpet: 
    def __init__(self, name: str, n, width, height):
        self.name = "Sierpinski Carpet"
        self.width = width
        self.height = height
        self.n = n

    def make_model(self):
        model = make_matrix(self.height, self.width)
        for j in range(1, self.height):
            for i in range(1, self.width):
                pixel = Pixel(i, j)
                pixel.filled_check(self.n)
                if pixel.filled == 1:
                    model[i][j] = WHITE
                else:
                    model[i][j] = BLACK
        
        return model

if __name__ == "__main__":
    scarp = SierpinskiCarpet("Sierpinski Carpet", 15, 729, 729)
    model = scarp.make_model()
    picture = MakeImage.from_pixel_colors(model)
    picture.show(scarp.name)