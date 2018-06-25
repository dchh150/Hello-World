import os
import shutil
import datetime


def my_mkdir(path_s):
    try:
        os.mkdir(path_s)
        return print("成功创建目录：", path_s)
    except FileExistsError as err:
        return print("目录已存在：", err)
    except FileNotFoundError as err:
        return print("创建失败：",err,"\n上一级目录不存在\n-----")


def main():
    today_ti = datetime.datetime.now()
    today = today_ti.strftime("%Y%m%d")    #'20180625'
    before14_ti = today_ti-datetime.timedelta(days=14)
    before14 = before14_ti.strftime("%Y%m%d")    #'20180611'
    mypath = 'E:/2017工作-ET/开网优化/进度统计/每周进度/'
    mytodaypath = mypath+today
    mybf14path = mypath+before14
    # 当天文件夹
    mypath2_li = ['/ftp', '/厂家反馈核查', '/发给厂家', '/建设维护类挂起工单', '/进度邮件']
    # 子文件夹
    copynames = [  #需要复制的文件，格式：日期用{}代替,开头需要/符号
        '/a{}',
        '/a{}',
    ]
    my_mkdir(mytodaypath)
    for each in mypath2_li:
        my_mkdir(mytodaypath + each)
        # 文件夹创建完成

    for n in copynames:
        try:
            shutil.copyfile(
                mytodaypath + n.format(before14),
                mybf14path + n.format(today)
            )
        except FileNotFoundError as err:
            print('复制错误,找不到原文件：\n', err)


if __name__ == '__main__':
    main()
