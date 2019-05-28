"""Part 1: Working with a Filesystem"""

# 4 C:/Users/Student Login/Desktop/nice.jpg
# 5 ../Users/Student Login/Desktop/nice.jpg

"""Part 2: Rendering an Image on Screen"""

'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation="none")
ax.set_xlim(40, 150)
ax.plot(37, 49, 'ro')
ax.plot(115, 40, 'ro')
ax.plot(140, 40, 'ro')
# Show the figure on the screen
# fig.show()
fig.savefig("experiment")

# 7 No, the code did not work.
# Now It did work, because it used Matplotlib in a way that is compatible with
# text.
# The coordinates of her nose are about (300, 400). The cat nose tip is at
# (60, 45)

# 8a fig is an instance of Figure, ax is an instance of AxesSubplot
# 8b The method safefig is being called on the object fig. That method is
# being given two arguments. That method is a method of the class Figure.
# 8c The line saves the figure object to cat_plot.png

# 9a The method imgshow is being called on the object ax[0]

"""Part 5: Keyword = Value Pairs"""

# 12 Another method is Axes.text, and an optional argument it takes is "fontdict",
# and it provides configuration for the text style.

"""Conclusion"""

# 1 Absolute filenames are absolute to the root folder, while relative filenames
# are relative to the current working directory (.)

# 2 An object is an instance of a class, which means that it is data with attributes
# and methods that falls into a class of objects.

# 3 Properties are data attributes of the object, and methods are functions that
# modify or return data based on these properties.

# 4 When you call a method on the object, a function is called that is given
# access to the object and any other arguments, and it can then modify the object
# itself or perform some function based on the object and arguments.