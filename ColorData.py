import os
import numpy
from PIL import Image, ImageDraw

#Add as command line argument
path = "/mnt/c/Users/Cody/Pictures/Wallpapers/"
filenum = 1
final_vals = []
for file in os.listdir(path):
    print("--------------------")
    img = Image.open(path + file)
    rgb_vals = numpy.asarray(img)
    rgb_avg = numpy.mean(rgb_vals, axis=(0, 1))
    rgb_avg = numpy.around(rgb_avg)
    rgb_avg = rgb_avg.astype(int)
    final_vals.append(tuple(rgb_avg))
    print(rgb_avg)
    print("file #" + str(filenum) + " of 38")
    filenum += 1 

print(final_vals)

#Add as command line arguments 
outfile_width = 1000
outfile_height = 500
color_width = outfile_width/len(final_vals)
#Coordinates for color rectangles to be drawn
cord1 = (0, 0)
cord2 = (color_width, 500)

#create new image for color rectangles to be drawn
img = Image.new(mode="RGB",size=(outfile_width, outfile_height))
draw = ImageDraw.Draw(img)
#Iterate through each color in the final color values array and draw a rectangle for that color
#Each rectangle is a given width to fill the width of the image
#Trying to find more efficient code than converting frol tuples to lists back to tuples
for i in range(0, len(final_vals)):
    draw.rectangle([cord1, cord2], fill=final_vals[i])
    cord1 = list(cord1)
    cord1[0] += color_width
    cord1 = tuple(cord1)
    cord2 = list(cord2)
    cord2[0] += color_width
    cord2 = tuple(cord2)
img = img.save("/mnt/c/Users/Cody/Pictures/testout2.png")