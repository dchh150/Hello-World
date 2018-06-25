import os
import shutil
import time

def my_mkdir(path_s):
    try:
        os.mkdir(path_s)
        return print("成功创建目录：",path_s)
    except FileExistsError as err:
        return print("目录已存在：",err)

def main():
    today = time.strftime("%Y%m%d")
    mypath = 'E:/2017工作-ET/开网优化/进度统计/每周进度/'+today
    mypath2_li=['/ftp','/厂家反馈核查','/发给厂家','/建设维护类挂起工单','/进度邮件']
    my_mkdir(mypath)
    for each in mypath2_li:
        my_mkdir(mypath + each)
    

if __name__ == '__main__':
    main()
        