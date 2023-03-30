#coding=utf-8

import sys
import os
import codecs
import chardet
##编码转换

def ReadFile(filePath,encoding="utf_8_sig"):
    with codecs.open(filePath,"r",encoding) as f:
          return  f.read()
 
def WriteFile(filePath,u,encoding="gb18030"):
    with codecs.open(filePath,"w",encoding) as f:
           f.write(u)

def UTF8_2_GBK(src,dst):
    content = ReadFile(src,encoding="utf-8")
    WriteFile(dst,content,encoding="gb18030")

def gbk_to_utf8(src, dst):
    if -1 != dst.find('VipChargeLayer.cpp') :
        print("dd")
    try:
        content = ReadFile(src,"gb18030")
        if None != content:
            WriteFile(dst,content,"utf_8_sig")
    except :
        content = ReadFile(src,"utf-8")
        if None != content:
            WriteFile(dst,content,"utf_8_sig")

def ucs_to_utf8(src, dst):
     content = ReadFile(src,"ucs_2")
     if None != content:
            WriteFile(dst,content,"utf_8_sig")

def to_utf8(src, dst):
    print(src)
    f = open(src, "rb")
    b = f.read()
    coding = chardet.detect(b)
    u = b.decode(coding["encoding"])
    s = u.encode("utf_8_sig")
    f.close()

    f = open(dst, "wb")
    f.write(s)
    f.flush()
    f.close();

    


argv1 = 'D:\\project\\007\\trunk\\client\\SubDragon\\SubDragon\\Classes\\' #os.getcwd()
#argv1 = "D:\\Classes\\"
'''argv2 = sys.argv[1]'''
argv2 = "c:\\new"


def genPath(root, path, pathList):
    dirlist = os.listdir(root + path)
    for f in dirlist:
       if os.path.isdir(root + path + "\\" + f) :
           str = path + '\\' + f
           genPath(root, str, pathList)
       else :
           pathList.append(path + '\\' + f)
            
def convertTo(path, src, to):
    dirlis = src.split('\\',)
    strP = to
    for i in range(len(dirlis) - 1) :
        if "" != dirlis[i] :
             strP = strP + '\\' + dirlis[i]
             if not os.path.isdir(strP) :
                 os.mkdir(strP)
    to_utf8(path + src, to+src)
    

pathList = []

genPath(argv1, "", pathList)

if not os.path.exists(argv2) :
    os.mkdir(argv2)
for f in pathList :
    convertTo(argv1, f, argv2)



