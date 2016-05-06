#-*- coding: utf-8 -*-
import os
from os.path import join
import shutil
import sys

reload(sys)
sys.setdefaultencoding(sys.getfilesystemencoding())
targetDir = unicode(os.getcwd())

def movefile(dirname, filelist):
    for file in filelist:
        print "MoveFile <" + join(dirname,file) + ">" + "--> <" + join(targetDir,file) +">"
        shutil.move(join(dirname,file), join(targetDir,file))
    shutil.rmtree(dirname)

def main():
    for root, dirs, files in os.walk(targetDir):
        if targetDir == root:
            continue
        movefile(root, files)

if __name__ == "__main__":
    input = raw_input(u"현재 실행하려는 경로가 " + unicode(os.getcwd()) + u"맞습니까?(Y/N)" )
    if input == 'y' or input == 'Y':
        main()


