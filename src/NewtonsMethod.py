from PIL import Image

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

img_x = 1024
img_y = 1024
image = Image.new("RGB", (img_x, img_y))

max_iterations = 25
epsilon = 0.1

for x in range(-256, img_x - 256):
    for y in range(-256, img_y - 256):
        a = -2 + 0.007 * x
        b = -2 + 0.007 * y
        for i in range(max_iterations):
            numerator = (((a ** 2 - b ** 2) ** 2 - 4 * a ** 2 * b ** 2 - 1) * 4 * (a ** 3 - 3 * a * b ** 2) + (4 * a * b * (a ** 2 - b ** 2) * 4 * (3 * a ** 2 * b - b ** 3)))
            denominator = (16 * (a ** 3 - 3 * a * b ** 2) ** 2 + 16 * (3 * a ** 2 * b - b ** 3) ** 2)
            x_n = a - numerator / denominator
            numerator = (((a ** 2 - b ** 2) ** 2 - 4 * a ** 2 * b ** 2 - 1) * (-4) * (3 * a ** 2 * b - b ** 3)) + 4 * (a ** 3 - 3 * a * b ** 2) * (4 * a * b * (a ** 2 - b ** 2))
            denominator = (16 * (a ** 3 - 3 * a * b ** 2) ** 2 + 16 * (3 * a ** 2 * b - b ** 3) ** 2)
            y_n = b - numerator / denominator
            a = x_n
            b = y_n

        if abs(a - 1) + abs(b) < epsilon:
            image.putpixel((x + 256, y + 256), BLUE)
        elif abs(a + 1) + abs(b) < epsilon:
            image.putpixel((x + 256, y + 256), RED)
        elif abs(a) + abs(b - 1) < epsilon:
            image.putpixel((x + 256, y + 256), GREEN)
        elif abs(a) + abs(b + 1) < epsilon:
            image.putpixel((x + 256, y + 256), YELLOW)
        
image.save("newton.png", "PNG")
