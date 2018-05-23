#!/usr/bin/env python3

from decimal import Decimal
import argparse
import MakeImage
import Matrix

BLACK = (0, 0, 0)
RED = (255, 0, 0)

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-W", "--width", help="Image width", default=1100)
    parser.add_argument("-H", "--height", help="Image height", default=700)
    parser.add_argument("-d", "--dpi", help="Image DPI", default=300)
    parser.add_argument("-r", "--real", help="The real component of the initial C value.")
    parser.add_argument("-i", "--imaginary", help="The imaginary component of the initial C value.")
    parser.add_argument("-f", "--filename", help="Filename to save to; if unspecified, show without saving.")
    args = parser.parse_args()
    missingArg = False
    if args.real is None:
        missingArg = True
        print("Fatal: No real component for C specified.")
    if args.imaginary is None:
        missingArg = True
        print("Fatal: No imaginary component for C specified.")
    if missingArg:
        quit()
    else: 
        args.real = Decimal(args.real)
        args.imaginary = Decimal(args.imaginary)
        return args


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
        model = Matrix.new(self.height, self.width)
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
    args = parseArgs()
    jset = JuliaSet("Julia Set", args.width, args.height, args.real, args.imaginary)
    model = jset.make_model()
    picture = MakeImage.from_pixel_colors(model)
    if args.filename is not None:
        picture.save(args.filename, format="PNG", dpi=(args.dpi, args.dpi))
        print("Saved image as " + args.filename)
    else:
        picture.show(title=jset.name)