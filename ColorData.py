import os
import numpy
from PIL import Image, ImageDraw

#Add as command line argument
path = "/mnt/c/Users/Cody/Pictures/Wallpapers/"
filenum = 0
final_vals = []
for file in os.listdir(path):
    print("--------------------")
    img = Image.open(path + file)
    rgb_vals = []
    r_total = 0
    g_total = 0
    b_total = 0

    #Iterate through each pixel of the provided image and append its pixel values to rgb_vals
      #This makes rgb_vals an array of tuples (ex: rgb_vals[(r_val, g_val, b_val), (r_val, g_val, b_val), etc.])
    for y in range(img.height):
        for x in range (img.width):
            rgb_vals.append(img.getpixel((x, y)))

    #add each r, g, b value to get an overall total
    for i in range(len(rgb_vals)):
        r_total += rgb_vals[i][0]
        g_total += rgb_vals[i][1]
        b_total += rgb_vals[i][2]

    #Average each r, g, b total with the number of pixels in the image to get an overall color
    r_avg = round(r_total/(img.height * img.width))
    g_avg = round(g_total/(img.height * img.width))
    b_avg = round(b_total/(img.height * img.width))

    final_vals.append(tuple((r_avg, g_avg, b_avg)))

    print(r_avg, g_avg, b_avg)
    filenum += 1

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
img = img.save("/mnt/c/Users/Cody/Pictures/testout.png")