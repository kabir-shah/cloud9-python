from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import numpy as np      # 'as' lets us use standard abbreviations
import os.path
import slash

"""Part 1: Using Arrays of Pixels"""

# 4 Lists can have different data types, arrays can't.

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'unsplash.jpg')
# Read the image data into an array
img = plt.imread(filename)

# 5 Height = 960, Width = 584, img[5][9][1] = 94, img[4][10][0] = 62,
# img[24][49][0] = 75

"""Part 2: Manipulating Pixels"""
fig, ax = plt.subplots(1, 2)

height = len(img)
width = len(img[0])

def change_color(img):
    img = img.copy()
    
    for r in range(155):
        for c in range(width):
            if sum(img[r][c]) > 500:
                img[r][c] = [255, 0, 255, 255]
                
    for r in range(420, 460):
        for c in range(115, 160):
            if (sum(img[r][c]) / 3) > 150:
                img[r][c] = [0, 0, 255, 255]
                
    return img
    
def make_mask():
    image = np.zeros((height, width, 4), dtype=np.uint8)
    
    slash.slashNoiseSeed()
    
    for r in range(height):
        for c in range(width):
            #image[r][c] = [slash.slashNoise2D(c * 4.3 + 10.0, r * 7.5 + 5.4) * 255, slash.slashNoise2D(c * 5.7 + 2.4, r * 6.3 + 9.23) * 255, slash.slashNoise2D(c * 6.7 + 4.6, r * 5.3 + 3.4) * 255]
            image[r][c] = img[int(slash.slashNoise2D(c * 2.3 + 10.0, r * 7.5 + 5.4) * height)][int(slash.slashNoise2D(c * 5.7 + 2.4, r * 6.3 + 9.3) * width)]
    
    return image
        
ax[0].imshow(change_color(img), interpolation='none')
ax[1].imshow(make_mask())
fig.savefig('1.4.3/experiment')

# 7a The algorithm checks the intensity of each color to make sure that it matches
# the brightness of the sky, and changes the matching pixels to be magenta.

"""Conclusion"""

# 1 An altered image is an image that is based off of calculations on a source
# image's pixels. If a digital image is altered, the pixels are changed based
# on a certain computation or for a certain effect.

# 2 Light sensitive film can capture more detail, but is restricted in terms of
# exposure or resolution. Digital cameras are flexible and have customizable
# resolutions, exposures, and various other settings for both photography
# and post production effects.

# 3a These six bits are responsible for the least significant place values that
# affect an RGB value very little.

# 3b 6 bits can encode 0-63 because 2^6 = 64, and 0-63 is a set of 64 numbers.

# 3c The image may lose color detail when it comes to very specific color differences.

# 4 An algorithm can identify different objects by using a threshold for differences
# in color to see how many borders there are that mark objects, and count them
# to provide the information to the library user.