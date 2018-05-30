#!/usr/bin/env python3

from decimal import Decimal
from PIL import Image
import argparse
import MakeImage
import Matrix

BLACK = (0, 0, 0)
RED = (255, 0, 0)
maxIter = 255

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-W", "--width", help="Image width", default=1500)
    parser.add_argument("-H", "--height", help="Image height", default=1040)
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
        args.real = float(args.real)
        args.imaginary = float(args.imaginary)
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
        self.r_start = r_start
        self.i_start = i_start
    
    def make_image(self):
        image = Image.new("RGB", (self.width, self.height), "white")
        for x in range(self.width):
            for y in range(self.height):
                zx = 1.5 * (x - self.width/2) / (0.5 * self.width)
                zy = 1.0 * (y - self.height/2) / (0.5 * self.height)
                i = 0
                while zx**2 + zy**2 < 4 and i < maxIter:
                    tmp = zx**2 - zy**2 + self.r_start
                    zy, zx = 2.0 * zx * zy + self.i_start, tmp
                    i += 1
                if i < maxIter:
                    image.putpixel((x,y), RED)
                else:
                    image.putpixel((x, y), BLACK)
        return image

if __name__ == "__main__":
    args = parseArgs()
    if args.height is not None and args.width is not None:
        jset = JuliaSet("Julia Set", args.width, args.height, args.real, args.imaginary)
    else:
        jset = JuliaSet("Julia Set", 1920, 1080, args.real, args.imaginary)
    
    image = jset.make_image()
    if args.filename is not None:
        image.save(args.filename, format="PNG")
        print("Saved image as " + args.filename)
    else:
        image.show(title=jset.name)