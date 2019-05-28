# 7a It takes two arguments, a PIL.Image and a corner radius. It returns
# a new PIL.Image with rounded corners.

# 7b Magenta

# 7c rounded_mask and drawing_layer

# 7d Alpha of 0

# 7e 41-47 for the circles, and 33-36 for the rectangles

# 7f Transparent black.

# 7g (0, 127, 127)

"""
8

a 0 or 1 arguments
b A list with a PIL.Image for each image, and a list with a string for each image name.
c os.listdir(), os.getcwd(), os.path.join()
d os.getcwd() Return a string representing the current working directory.
e It uses a try/except to throw and report an error if reading the images or directory failed. This had advantages because errors can easily be handled.
f It does nothing with errors.
"""

"""
9

a Making a directory can fail.
b The number of images in the directory.
c The index of the image in the directory.
"""

"""
Conclusion

1 This is accomplished by using an algorithm with trigonometric functions for calculating an arc on each end of the polygon window (rectangle).

2 This made reuse easier because it separated different areas of logic into different functions and reduced the cognitive load of the code.

3 It all depends on the definition of manipulation. Alice is right given that manipulation means any sort of pixelation. Bob is right given that manipulation means changing the meaning or purpose of an image. 

4 An image is yours to distribute if you are the one that was responsible for generating it or taking it. 

5 We all understood the code and were able to understand the questions easily.
"""
