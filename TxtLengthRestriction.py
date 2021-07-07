import re
import codecs
import sys
import os
path = "C:\zl\Workplace\pachong\FandomPC\\Description_shorter"
FileNameList = os.listdir(path)  # 取路径下的文件名，生成列表
Length=200
for FileName in FileNameList:  # 遍历列表下的文件名
    print(FileName)
    delpath=path+"\\"+FileName
    shorter_data = ""
    with open(delpath, "r", encoding="UTF-8") as f:
            data = f.read()

    if len(data)>Length:
        data_list=data.split('.')

        for data_piece in data_list:
            shorter_data+=data_piece+'.'
            if len(shorter_data)>Length:
                break;
    if len(data) > Length+200:
        shorter_data = ""
        data_list = data.split(' ')

        for data_piece in data_list:
            shorter_data += data_piece + ' '
            if len(shorter_data)>Length:
                break;
    else:
        shorter_data=data

    shorter_data=shorter_data.replace('\n','').replace(' .', '.')

    #Delete first space
    spacecount=0
    for i in shorter_data:
        if i ==' ':
            spacecount+=1
        else:
            break
    shorter_data=shorter_data[spacecount:len(shorter_data)]
    print(shorter_data)

    #Write in file
    with open(delpath, "w", encoding="utf-8") as f:
        f.write(shorter_data)