#!/usr/bin/env python3
#Author: Evan Sean DesRosiers

import os
import shutil

filename = input("What file do you want to print the contents of?") #accepts user input for filename
contents = open(filename, 'r') #opens and reads file contents, assigning to variable "contents"
print(contents.read()) #prints the read contents

#if filename == teams:

#    team = input("Please select from the following options:\nA: List Teams\nB: List team abbreviations\nC: List cities
