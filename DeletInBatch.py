import imghdr
import os
#获取所要操作的文件夹(换成你的文件夹路径)
filepath = "C:\\Users\\aaa\\Desktop\\ptest"
#获取文件夹内的照片名列表
name_list = os.listdir(filepath)
#创建删除记录文本文件
fp=open(filepath+"\\删除记录.txt", "a+")
#循环文件名列表
for name in name_list:
    #拼接照片的绝对路径
    delpath = filepath + "\\" + name
    #判断文件是否损坏
    if not imghdr.what(delpath) :
        # 如果损坏，则进行删除
        os.remove(delpath)
        #然后把删除操作记录写入文本中（内存）
        fp.write(filepath + "\\" + name+'\n')
        #最后进行刷新操作，把内存中的数据保存到文本文件中
        fp.flush()