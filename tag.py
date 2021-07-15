# Quick and dirty script to add tags to all your pictures using exiftool. This may help to improve your ranking
# Use a file (by default meta.json) with the values you want to set in all your images
# Specify a folder and have fun
# You need to install exiftool and obviously python
#
# Example: python tag.py --input 'pictures_folder' --file 'meta.json'
#
# www.josepalma.ca 
# Just an extra line to test

from os import listdir
from os.path import isfile, join
import os
import argparse
import json
import subprocess

parser = argparse.ArgumentParser(description='Process exif data in batch')
parser.add_argument('-f', '--file', action='store', dest='file', help='input file', default='meta.json')
parser.add_argument('-i', '--input', action='store', dest='input', help='input folder', default='.')

options = parser.parse_args()

configuration_file = open(options.file,)
data = json.load(configuration_file)

current_path = options.input

if not os.path.isabs(current_path):
    current_path = os.path.realpath(current_path)

onlyfiles = [f for f in listdir(current_path) if isfile(join(current_path, f))]

base_command = ['exiftool']
for key,value in data.items():
    base_command.extend(['-' + key + '=' + value])


for image in onlyfiles:
    new_command = base_command.copy()
    new_command.extend([join(current_path, image)])
    subprocess.run(new_command)

