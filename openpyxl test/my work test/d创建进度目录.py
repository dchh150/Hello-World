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
        return print("创建失败：", err, "\n上一级目录不存在\n-----")


def main():
    today_ti = datetime.datetime.now()
    today = today_ti.strftime("%Y%m%d")  # '20180625'
    before7_ti = today_ti-datetime.timedelta(days=7)
    before7 = before7_ti.strftime("%Y%m%d")  # '20180618'
    mypath = 'E:/2017工作-ET/开网优化/进度统计/每周进度/'
    mytodaypath = mypath+today
    mybf7path = mypath+before7
    # 当天文件夹
    mypath2_li = ['/ftp', '/厂家反馈核查', '/发给厂家',
                  '/建设维护类挂起工单', '/进度邮件', '/发给厂家/厂家周四反馈']
    # 创建的子文件夹
    copynames = [  # 需要复制的文件，格式：日期用{}代替,开头需要/符号；
        '/过程管控周报统计-{}-有fdd.xlsx',
        '/每日质量通报统计{}-新版本-无fdd.xlsx',
        '/进度邮件/过程管控指标周报V9-{}.xlsx',
        '/进度邮件/开网优化进展,验收工作进度情况,各期锁定进度情况_{}.docx',
        '/进度邮件/每日质量通报{}.xlsx',
        '/发给厂家/附件一：21地市单优形象进度原因解析-{}.xlsx',
        '/厂家反馈核查/添加前缀_厂家.bat',
        '/各文件夹材料备忘.txt'
    ]
    my_mkdir(mytodaypath)
    for each in mypath2_li:
        my_mkdir(mytodaypath + each)
        # 文件夹创建完成

    for n in copynames:
        try:
            shutil.copyfile(
                mybf7path + n.format(before7),
                mytodaypath + n.format(today)
            )
            print("完成复制：", n.format(before7))
        except FileNotFoundError as err:
            print('复制错误,找不到原文件：\n', err)

    input('操作完成，按任意键退出:')


if __name__ == '__main__':
    main()
