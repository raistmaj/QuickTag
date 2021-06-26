# Quick and dirty script to add tags to all your pictures using exiftool. This may help to improve your ranking
# Use a file (by default meta.json) with the values you want to set in all your images
# Specify a folder and have fun
# You need to install exiftool and obviously python
#
# Example: python tag.py --input 'pictures_folder' --file 'meta.json'
#
# www.josepalma.ca 
from os import listdir
from os.path import isfile, join
import math
import os
import argparse
import json
import pathlib
import subprocess

parser = argparse.ArgumentParser(description='Process exif data in batch')
parser.add_argument('-f', '--file', action='store', dest='file', help='input file', default='meta.json')
parser.add_argument('-i', '--input', action='store', dest='input', help='input folder', default='.')

options = parser.parse_args()

configuration_file = open(options.file,)
data = json.load(configuration_file)

gpslat = data['latitude']
gpslon = data['longitude']

current_path = options.input

if not os.path.isabs(current_path):
    current_path = os.path.realpath(current_path)

onlyfiles = [f for f in listdir(current_path) if isfile(join(current_path, f))]

for image in onlyfiles:
    subprocess.run(['exiftool', '-GPSLongitude='+gpslon, '-GPSLongitudeRef='+gpslat, '-GPSLatitude='+gpslon, '-GPSLatitudeRef='+gpslat, join(current_path,image)])

