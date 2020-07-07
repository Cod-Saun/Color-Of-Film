import os
from PIL import Image

#add as command line argument
path = "/mnt/c/Users/Cody/Pictures/Wallpapers/"
filenum = 0
for file in os.listdir(path):
    print("--------------------")
    img = Image.open(path + file)
    #img = Image.open('/mnt/z/Cody/Pictures/Photos/IMG_1012.JPG')
    rgb_vals = []
    r_total = 0
    g_total = 0
    b_total = 0

    for i in range(img.height):
        for x in range (img.width):
            rgb_vals.append(img.getpixel((x, i)))

    for i in range(len(rgb_vals)):
        r_total += rgb_vals[i][0]
        g_total += rgb_vals[i][1]
        b_total += rgb_vals[i][2]

    r_avg = round(r_total/(img.height * img.width))
    g_avg = round(g_total/(img.height * img.width))
    b_avg = round(b_total/(img.height * img.width))

    print(r_avg)
    print(g_avg)
    print(b_avg)
    
    out = Image.new(mode="RGB",size=(100,100),color=(r_avg,g_avg,b_avg))
    filename = "/mnt/c/Users/Cody/Pictures/Outfiles/out%d.jpg" %filenum
    out = out.save(filename)
    filenum += 1