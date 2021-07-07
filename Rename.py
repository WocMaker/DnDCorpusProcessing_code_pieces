import imghdr
import os
import re
import codecs
import sys
general_path = "C:\\zl\\Workplace\\classfolder_renamed"
folder_list = os.listdir(general_path)
for foldername in folder_list:
    path= general_path + "\\" + foldername
    old_names = os.listdir(path)  # 取路径下的文件名，生成列表
    count_img=1
    count_txt=1
    for old_name in old_names:  # 遍历列表下的文件名
        delpath=path+"\\"+old_name
        if ".jpg" in old_name:
            new_name = foldername+"."+str(count_img)+".jpg"

            os.rename(os.path.join(path, old_name), os.path.join(path, new_name))  # 子文件夹重命名
            print(old_name, "has been renamed successfully! New name is: ", new_name)  # 输出提示
            count_img += 1
        else:
            new_name = foldername + "." + str(count_txt)+".txt"

            os.rename(os.path.join(path, old_name), os.path.join(path, new_name))  # 子文件夹重命名
            print(old_name, "has been renamed successfully! New name is: ", new_name)  # 输出提示
            count_txt += 1

print("process finished")
