import re
import codecs
import sys
import os
general_path = "C:\zl\Workplace\classfolder_one_word"
folder_list = os.listdir(general_path)
for foldername in folder_list:
    path= general_path + "\\" + foldername
    old_names = os.listdir(path)  # 取路径下的文件名，生成列表
    count_img=1
    count_txt=1
    for old_name in old_names:  # 遍历列表下的文件名
        delpath=path+"\\"+old_name
        if ".txt" in old_name:
            file_data = ""
            with open(delpath, "r", encoding="gbk") as f:
                    line=old_name
                    cop = re.compile("[^a-z^A-Z^ ^]")
                    line = cop.sub('', line)
                    line = line.replace("fantasy character","").replace("fantasy","").replace("art","").replace("txt","")
                    file_data += line
            with open(delpath, "w", encoding="utf-8") as f:
                f.write(file_data)