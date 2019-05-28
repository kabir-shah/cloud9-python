from __future__ import print_function
import colorsys
import PIL
import PIL.Image
import numpy as np

image = np.array(PIL.Image.open("./images/Obama.jpg").convert("RGB"), dtype=float)

colors_length = 7
hues = np.random.rand(colors_length)
saturations = np.random.rand(colors_length)
lightnesses = np.random.rand(colors_length)

"""
hues = np.array([0.0, 0.0])
saturations = np.array([0.0, 1.0])
lightnesses = np.array([0.0, 1.0])
"""

def rgb_to_hsl(rgb):
	hls = colorsys.rgb_to_hls(*np.divide(rgb, 255.0))
	return hls[0], hls[2], hls[1]
	
def hsl_to_rgb(h, s, l):
	return np.multiply(np.array(colorsys.hls_to_rgb(h, l, s), dtype=float), 255.0)
	
"""
def change_pixel(x, y, n_hs, n_l):
	if y in image and x in image[y]:
		rgb = image[y, x]
		hs, l = rgb_to_hsl(rgb)
		avg_hs = np.divide(np.add(hs, n_hs), 2.0)
		avg_l = (l + n_l) / 2.0
		image[y, x] = hsl_to_rgb(avg_hs, avg_l)
		
error_hs = {}
error_l = {}

def average_error(x, y, error):
	surrounding_error = [error[e_x, e_y] for e_x, e_y in [(x - 1, y), (x - 1, y - 1), (x, y - 1)] if (e_x, e_y) in error_hs]
	length = len(surrounding_error)
	return 0.0 if length == 0 else sum(surrounding_error) / length

def pixel_old(c_x, c_y):
	x = image[c_y, c_x]
	x_hs, x_l = rgb_to_hsl(x)
	x_hs = np.sum(x_hs) + average_error(c_x, c_y, error_hs)
	x_l = x_l + average_error(c_x, c_y, error_l)
	
	y_hs = colors[np.argmin(colors_total - x_hs)]
	#y_hs = colors[np.argmin((colors_total - average_pixels(c_x, c_y, x_hs)) ** 2)]
	#y_hs = colors[np.argmin(np.square(np.subtract(colors_total, np.sum(x_hs))))]
	#y_l = lightnesses[np.argmin(np.square(np.subtract(lightnesses, x_l)))]
	y_l = lightnesses[np.argmin(lightnesses - x_l)]
	y = hsl_to_rgb(y_hs, y_l)
	error_hs[(c_x, c_y)] = x_hs - np.sum(y_hs)
	error_l[(c_x, c_y)] = x_l - y_l
	
	#change_pixel(c_x - 1, c_y, y_hs, y_l)
	#change_pixel(c_x + 1, c_y, y_hs, y_l)
	#change_pixel(c_x, c_y - 1, y_hs, y_l)
	#change_pixel(c_x, c_y + 1, y_hs, y_l)
	#change_pixel(c_x - 1, c_y - 1, y_hs, y_l)
	#change_pixel(c_x - 1, c_y + 1, y_hs, y_l)
	#change_pixel(c_x + 1, c_y - 1, y_hs, y_l)
	#change_pixel(c_x + 1, c_y + 1, y_hs, y_l)
	
	return y
"""
	
index = np.array([
	[0, 8, 2, 10],
	[12, 4, 14, 6],
	[3, 11, 1, 9],
	[15, 7, 13, 5]
], dtype=float) / 16.0

def pixel(c_x, c_y):
	threshold = index[c_y % 4, c_x % 4]
	x_h, x_s, x_l = rgb_to_hsl(image[c_y, c_x])
	
	y_hs = np.argsort(np.abs(hues - x_h))
	y_ls = np.argsort(np.abs(lightnesses - x_l))
	
	y_h_1 = hues[y_hs[0]]
	y_h_2 = hues[y_hs[1]]
	
	y_l_1 = lightnesses[y_ls[0]]
	y_l_2 = lightnesses[y_ls[1]]
	
	y_h = y_h_1 if ((x_h - y_h_1) / (y_h_2 - y_h_1)) < threshold else y_h_2
	y_s = saturations[y_hs[0]] if y_h == y_h_1 else saturations[y_hs[1]]
	y_l = y_l_1 if ((x_l - y_l_1) / (y_l_2 - y_l_1)) < threshold else y_l_2
	
	return hsl_to_rgb(y_h, y_s, y_l)

for y in range(len(image)):
	for x in range(len(image[y])):
		image[y, x] = pixel(x, y)
	print(str(float(y) / float(len(image)) * 100.0) + "%")
	
x_length = len(image[0])
y_length = len(image)
PIL.Image.fromarray(image.astype(np.uint8)).save("project.png")