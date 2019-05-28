'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import PIL
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'student.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.savefig('girl')

# Open, resize, and display earth
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.savefig('resize_earth')

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966), mask=earth_small) 
student_img.paste(earth_small, (705, 938), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('earth_as_eyes')

# 13 plt is for making mathematical plots, numpy is for number, vector, and matrix mathematics and manipulation, and PIL is for image manipulation.

# 15a Line 19 calls the function subplots() from the plt library. The function is being called with two arguments. The function returns two objects, which are being assigned to fig and ax.
# 15b Line 20 calls imshow on ax[0]
# 15b Line 23 calls imshow on ax[1]
# 15b Line 24 calls set_xticks on ax[1]
# 15b Line 25 calls set_xlim on ax[1]
# 15b Line 26 calls set_ylim on ax[1]
# 15b Line 27 calls savefig on fig
# 15c Upper left corner (1162, 966)

# 16 (706, 941) (790, 941) (706, 1010) (790, 1010) Height: 69, Width: 84

# 17a It is being passed 2 arguments. The value it returns is assigned to the variable earth_file.
# 17b Being assigned to the variable earth_img.
# 17c Tuples take parenthesis, and so do function calls.
# 17d The argument specifies the size for the earth so that the size matches the iris bounding box dimensions.
# 17e
"""
Line 33 calls the function subplots from the library plt with arguments 1, 2. The function returns 2 objects, which are being assigned to fig2, axes2.
Line 34 calls imshow method on the object axes2[0] with argument earth_img.
Line 35 calls imshow method on object axes2[1] with argument earth_small.
Line 36 calls the savefig method on object fig2 with argument "resize_earth".
"""
# 17f The optional argument is filter, which is NEAREST by default. This is also the recommended value for downsampling.
# 17g The first prints the width and height of the earth image, the second prints the width and height of the resized image, and the third prints the height of the earth image.
# 17i One is distorted and uses bigger pixels, meaning that there are less pixels to cover the same area.

# 18 Each pixel samples the surrounding pixels to create its' own value, creating a lower quality image because detail is lost and replaced with averages.

# 19a student_img bytes = 1920 * 2720 * 3 = 15667200
# 19a earth_small bytes = 89 * 87 * 4 = 30972
# 19c student_img = 211546, earth_small = 18774.
# 19d This may be because of compression in both jpg and png files.
# 19e If a color is the first argument, a solid color will be pasted.
# 19f The pasted image is converted to the mode of the first image.
# 19g Uses the earth_small image at the specified coordinates, and uses the alpha with the mask parameter.

"""Conclusion"""

# 1 The classes used were PIL.Image and matplotlib.axes.AxesSubplot. The methods specifically used for this were .paste(), which pasted an image into the specified coordinates of the upper left corner. An attribute we used was .size, which specified a tuple of the height and width of a PIL image.
# 2 An abstraction provided by the PIL library helped generalize the process of updating raw image data and interpolating it. It also helped provide an abstraction over image data that had the ability to generalize a data structure and write it to a specific file type without having to worry about the format.