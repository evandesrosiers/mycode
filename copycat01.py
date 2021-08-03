#!/usr/bin/env python3
# Author: Evan Sean DesRosiers Date/Time started: 03AUG2021@1130EST

def main():
    import shutil #file operations
    import os #imports operating system commands
    os.chdir("/home/student/mycode/") #changes directory to home directory
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy") #creates copy of file
    shutil.copytree("5g_research/", "5g_research_backup/") #copies folder and all folders/files within

main()
