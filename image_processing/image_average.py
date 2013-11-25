import Image
import numpy
import webcolors
import sys
import csv
import os

# Constants

NEWSIZE = 500

CSV_PATH = '../data/photodata/colordata.csv'
IMAGE_DIR = '../data/photodata/images'

# Make an array of all the filenames that have already been processed #

hexdict = csv.DictReader(open(CSV_PATH, 'rb'))
hexwriter = csv.writer(open(CSV_PATH, 'ab'))

processed_files = []

for row in hexdict:
    processed_files.append(row['filename'])

print "We've already processed these files" + str(processed_files)


# Make a list of the names of all the files in the directory #

present_files = []
os.chdir(IMAGE_DIR)
for file in os.listdir("."):
    if file.endswith(".jpg"):
        present_files.append(file)

print "These are the images available to process" + str(present_files)


# Find the files that are present but not processed.#
# Make a list of those, so they can _be_ processed.#

files_to_process = list(set(present_files) - set(processed_files))

print "We'll be processing the following" + str(files_to_process)



# The actual image processing #

def getDate(path):
    im = Image.open(path)
    exif_data = im._getexif()
    date = exif_data[36867]
    return date

def getAvgHex(path):
    im = Image.open(path)

    smaller_img = im.resize((NEWSIZE,NEWSIZE))
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

    return webcolors.rgb_to_hex(average_color)

for file in files_to_process:
    print file
    hexwriter.writerow([getDate(file),file,getAvgHex(file)])
