#!/usr/bin/env python3
#Written by Evan Sean DesRosiers on 03AUG2021@1210EST

def main():
    import shutil #brings in file manipulation commands
    import os #brings in command line commands
    os.chdir('/home/student/mycode/') #starts program in home directory
    shutil.move('raynor.obj', 'ceph_storage/') #moves raynor.obj to ceph_storage directory
    xname = input('What is the new name for kerrigan.obj?') #asks for new name of kerrigan.obj
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) #reanmes kerrigan.obj with user input

main()
