from PIL import Image

# -1 <= x <= 1
x_min = -2.0
x_max = 2.0

# -1 <= y <= 1
y_min = -2.0
y_max = 2.0

# max_iterations
max_iterations = 40

# Epsilon for error range
epsilon = 10e-5

# Red, Blue, Yellow, Green
colors = [(255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 0)]
# If you want to test different functions, add them (and their derivatives) here
# and call them at the bottom like the example
def fourth(z): 
	return (z**4 - 1)
	
def dfourth(z): 
	return (4 * z**3)

# Implementation of Newton's Method for derivate estimation
def newtons_method(f, f_prime, z):
	for i in range(max_iterations):
		z_plus = z - f(z) / f_prime(z)
		
		# Check for overflow
		if abs(f(z)) > 10e10:
			return None
		
		# Check for underflow
		if abs(f(z)) < 10e-14:
			return None
			
		# Checks for convergence
		if abs(z_plus - z) < epsilon:
			return z
		
		z = z_plus
		
	return None
	
# Method to graphically represent Newton's Method
def draw(f, f_prime, img, size, img_name):
	
	roots = []
	for y in range(size):
		z_y = y * (y_max - y_min)/(size - 1) + y_min
		for x in range(size):
			z_x = x * (x_max - x_min)/(size - 1) + x_min
			root = newtons_method(f, f_prime, complex(z_x, z_y))
			if root:
				flag = False
				for test_root in roots:
					if abs(test_root - root) < 10e-4:
						root = test_root
						flag = True
						break
				if not flag:
					roots.append(root)
			if root:
				img.putpixel((x, y), colors[roots.index(root) % 4])
	img.save(img_name, "PNG")
	
size = 1024
img = Image.new("RGB", (size, size), (0, 0, 0))
draw(lambda z: fourth(z), lambda z: dfourth(z), img, size, "test.png")

