import os
from PIL import Image

#add as command line argument
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

    print(r_avg)
    print(g_avg)
    print(b_avg)
    
    out = Image.new(mode="RGB",size=(100,100),color=(r_avg,g_avg,b_avg))
    filename = "/mnt/c/Users/Cody/Pictures/Outfiles/out%d.jpg" %filenum
    out = out.save(filename)
    filenum += 1

#add as command line arguments
print(final_vals)
outfile_width = 500
outfile_height = 1000