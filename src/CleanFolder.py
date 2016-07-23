#-*- coding: utf-8 -*-
import os
import sys
import shutil

reload(sys)
sys.setdefaultencoding('cp949')

video_extension = [".avi", ".wmv", ".mp4", ".mov"]

def get_file(target):
    target_folder = "./" + target
    exist_video = False
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            for ext in video_extension:
                if os.path.splitext(file)[1] == ext:
                    exist_video = True
                    shutil.move(target_folder+"/"+ file.decode('cp949'), "./")

    if exist_video == True:
        shutil.rmtree(target_folder)

def clean_file():
    for root, dirs, files in os.walk('./'):
        for dir in dirs:
            get_file(dir)

clean_file()
