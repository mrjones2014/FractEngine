from decimal import Decimal
import MakeImage

BLACK = (0, 0, 0)
RED = (255, 0, 0)

def make_matrix(w, h):
    return [[0 for x in range(w)] for y in range(h)]

def put_pixels(image, pixels, height, width):
    for x in range(width):
        for y in range(height):
            image.putpixel((x, y), pixels[x][y])

class JuliaSet:
    def __init__(self, name: str, width, height, r_start, i_start):
        sign = None 
        if i_start < 0:
            sign = ""
        else:
            sign = "+"
        self.name = "Julia Set, C={}".format("{}{}{}".format(r_start, sign, i_start))
        self.width = width
        self.height = height
        self.r_start = Decimal(r_start)
        self.i_start = Decimal(i_start)
    
    def make_model(self):
        model = make_matrix(self.height, self.width)
        for j in range(1, self.height):
            for i in range(1, self.width):
                r_old = Decimal(-1.6 + i / 320)
                i_old = Decimal(-1.1 + j / 320)
                for _ in range(0, 50):
                    r_new = Decimal(Decimal(r_old**2)-Decimal(i_old**2)+self.r_start)
                    i_new = Decimal(2*r_old*i_old+self.i_start)
                    r_old = r_new
                    i_old = i_new
                    if (r_new**2 + i_new**2 > 2):
                        break
                
                result = Decimal(r_new**2)+Decimal(i_new**2)
                if (result < 2):
                    model[i][j] = BLACK
                else:
                    model[i][j] = RED
        return model

if __name__ == "__main__":
    jset = JuliaSet("Julia Set", 1100, 700, -0.123, 0.745)
    model = jset.make_model()
    picture = MakeImage.from_pixel_colors(model)
    picture.show(jset.name)