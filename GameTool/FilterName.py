#coding=utf-8
import sys
import os
import codecs

paths = 'D:\\project\\007\\trunk\\client\\win_yiTian\\yiTian2\\Classes\\'

files = os.listdir(paths)

tStr = ''

filesList = []

for f in files:
    if os.path.isfile(paths + f):
        if '.' != f[0] and -1 != f.rfind('.pb.cc'):
            filesList.append(f)

for f in filesList:
    tStr += '../../yiTian2/Classes/' + f + ' '

print(tStr);

             