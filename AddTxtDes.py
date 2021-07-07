import imghdr
import os
import re
import codecs

#获取所要操作的文件夹(换成你的文件夹路径)
filepath = "C:\\zl\\Workplace\\basic_pair_12k"
#获取文件夹内的照片名列表
name_list = os.listdir(filepath)
#初始化计数器
cont=1
#循环文件名列表
for name in name_list:
    cont+=1
    #拼接图片的绝对路径
    delpath = filepath + "\\" + name
    #生成的文本的路径
    txtpath = delpath.replace('.jpg', '.txt')
    if imghdr.what(delpath):
        #处理文本
        des=name.replace('.jpg', '').replace('  ', '').replace('+', ' ').replace('ArtStation', '').replace('Twitter','')
        cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^ ]")
        des=cop.sub('',des)
        with open(txtpath, "w") as f:
            f.write(des)
    print('processing number'+str(cont))
print('process finished')