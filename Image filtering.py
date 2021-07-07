from PIL import Image
import imghdr
import os
import re
import codecs
import sys
general_path = "C:\zl\Workplace\classfolder_renamed_filtered"
folder_list = os.listdir(general_path)
for foldername in folder_list:
    path= general_path + "\\" + foldername
    old_names = os.listdir(path)  # 取路径下的文件名，生成列表
    count_img=1
    for old_name in old_names:  # 遍历列表下的文件名
        delpath=path+"\\"+old_name
    try:
        img = Image.open(delpath)
    except:
        os.remove(delpath)
        print("delete"+str(old_name))
    print("finish folder"+str(foldername))