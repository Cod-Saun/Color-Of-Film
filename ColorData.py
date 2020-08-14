import os
import sys
import numpy
from PIL import Image, ImageDraw

if len(sys.argv) < 5:
    print("Too few arguments recieved: must provide path to images directory and final image")
    print("python Colordata.py [path to images] [path to output file] [width of final image] [height of final image]")
    sys.exit()
if len(sys.argv) > 5:
    print("Too many arguments recieved.")
    print("python Colordata.py [path to images] [path to output file]")
    sys.exit()

path = sys.argv[1]
finalpath = sys.argv[2]
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
    print("file #" + str(filenum))
    filenum += 1 

#Add as command line arguments 
outfile_width = sys.argv[3]
outfile_height = sys.argv[4]
color_width = int(outfile_width)/len(final_vals)
#Coordinates for color rectangles to be drawn
cord1 = (0, 0)
cord2 = (color_width, int(outfile_height))

#create new image for color rectangles to be drawn
img = Image.new(mode="RGB",size=(int(outfile_width), int(outfile_height)))
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
img = img.save(finalpath)