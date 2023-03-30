import sys
import os
import codecs

strSrc = "D:\\project\\007\\trunk\\client\\win_yiTian\\yiTian2\\proto\\"
strDest = "C:\\proto\\"

files = os.listdir(strSrc)
for f in files:
    if -1 != f.rfind('.proto') and not os.path.isdir(f):
        protoF = codecs.open(strSrc + f, 'r', 'utf-8')
        strContent = protoF.read()
        protoF.close()
        strContent = strContent.replace('LITE_RUNTIME', 'SPEED',1)

        protoW = codecs.open(strDest + f, 'w', 'utf-8')
        protoW.write(strContent)
        protoW.close()
            
