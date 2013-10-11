# process image to extract color
# given a file name, return a HEX value

# make a dict of: 
# timestamp, filename, HEX value

import Image
import numpy
import webcolors

desired_size = 500

im = Image.open('./assets/images/test-2.jpg')
smaller_img = im.resize((desired_size,desired_size))
size = smaller_img.size[0]

pix = smaller_img.load()

all_rgb_values = []

for x in range(0,size):
    for y in range(0,size): 
        all_rgb_values.append(pix[x,y])

red_list = []
green_list = []
blue_list = []

for index in range(0,size):
    red_list.append(all_rgb_values[index][0])
    green_list.append(all_rgb_values[index][1])
    blue_list.append(all_rgb_values[index][2])

red_avg = numpy.mean(red_list)
green_avg = numpy.mean(green_list)
blue_avg = numpy.mean(blue_list)

average_color = (int(red_avg), int(green_avg), int(blue_avg))

print webcolors.rgb_to_hex(average_color)
