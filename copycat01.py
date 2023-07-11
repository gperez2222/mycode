#!/usr/bin/env python3

""" The module shutil is one of those not so common tools, and the way to make it accessible is with the import statement. """

import shutil

""" This module provides a portable way of using operating system dependent functionality. Where shutil allows for higher-level 
file manipulation, os is more targeted at the operating system."""

import os

""" os.chdir(). This will allow the user to run the program from any location on the system, and our script still always 
start at /home/student/mycode/ """

# move into the working directory
os.chdir("/home/student/mycode/")

""" Calling, shutil.copy(source, destination) will copy the file at the path source to the folder at the path destination. 
(Both source and destination are strings.) If destination is a filename, it will be used as the new name of the copied file. 
This function returns a string of the path of the copied file. """

# copy the fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")


""" The shutil.copy() will copy a single file, whereas shutil.copytree() will copy an entire folder and every folder and file contained in it. 
Calling shutil.copytree(source, destination) will copy the folder at the path source, along with all of its files and subfolders, to the folder 
at the path destination. The source and destination parameters are both strings. The function returns a string of the path of the copied folder. """

# copy the entire directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")

